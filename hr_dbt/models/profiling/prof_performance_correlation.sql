{{ config(materialized='table') }}

with employee_metrics as (
    select
        e.employee_id,
        e.salary,
        e.employment_status,
        d.department_name,
        dv.division_name,
        date_part('year', age(current_date, e.hire_date))           as tenure_years,
        avg(pr.performance_score)                                    as avg_perf_score,
        stddev_pop(pr.performance_score)                             as perf_score_stddev,
        count(pr.review_id)                                          as review_count,
        sum(case when tr.passed = 'Yes' then 1 else 0 end)          as trainings_passed,
        count(tr.training_id)                                        as trainings_total,
        round(
            (sum(case when tr.passed = 'Yes' then 1 else 0 end)::numeric
             / nullif(count(tr.training_id), 0) * 100), 2
        )                                                            as training_pass_rate,
        avg(att.attendance_rate_pct)                                 as avg_attendance_pct
    from {{ ref('stg_employees') }} e
    join {{ ref('stg_departments') }}       d   using (department_id)
    join {{ ref('stg_divisions') }}         dv  using (division_id)
    left join {{ ref('stg_performance_reviews') }} pr using (employee_id)
    left join {{ ref('stg_training_records') }}    tr using (employee_id)
    left join {{ ref('stg_attendance_summary') }}  att using (employee_id)
    group by e.employee_id, e.salary, e.employment_status,
             d.department_name, dv.division_name,
             e.hire_date
)

select
    division_name,
    count(employee_id)                                               as n,
    round(corr(avg_perf_score, salary)::numeric, 4)                 as perf_salary_corr,
    round(corr(avg_perf_score, tenure_years)::numeric, 4)           as perf_tenure_corr,
    round(corr(avg_perf_score, training_pass_rate)::numeric, 4)     as perf_training_corr,
    round(corr(avg_perf_score, avg_attendance_pct)::numeric, 4)     as perf_attendance_corr,
    round(corr(salary, tenure_years)::numeric, 4)                   as salary_tenure_corr,
    round(corr(training_pass_rate, avg_attendance_pct)::numeric, 4) as training_attendance_corr,
    round(avg(avg_perf_score)::numeric, 3)                          as avg_perf_score,
    round(avg(salary)::numeric, 2)                                  as avg_salary,
    round(avg(tenure_years)::numeric, 2)                            as avg_tenure_years,
    round(avg(training_pass_rate)::numeric, 2)                      as avg_training_pass_rate_pct,
    round(avg(avg_attendance_pct)::numeric, 2)                      as avg_attendance_pct
from employee_metrics
group by division_name
order by division_name
