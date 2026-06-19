{{ config(materialized='table') }}

select
    d.department_name,
    dv.division_name,
    j.job_title,
    count(e.employee_id)                                        as headcount,
    round(avg(e.salary)::numeric, 2)                           as avg_salary,
    round(stddev_pop(e.salary)::numeric, 2)                    as salary_stddev,
    min(e.salary)                                              as salary_min,
    round(percentile_cont(0.25) within group (order by e.salary)::numeric, 2) as salary_p25,
    round(percentile_cont(0.50) within group (order by e.salary)::numeric, 2) as salary_median,
    round(percentile_cont(0.75) within group (order by e.salary)::numeric, 2) as salary_p75,
    round(percentile_cont(0.90) within group (order by e.salary)::numeric, 2) as salary_p90,
    max(e.salary)                                              as salary_max,
    round((max(e.salary) - min(e.salary))::numeric, 2)        as salary_range,
    round(
        (stddev_pop(e.salary) / nullif(avg(e.salary), 0) * 100)::numeric, 2
    )                                                          as salary_cv_pct
from {{ ref('stg_employees') }} e
join {{ ref('stg_departments') }} d  using (department_id)
join {{ ref('stg_divisions') }}  dv using (division_id)
join {{ ref('stg_jobs') }}       j  using (job_id)
where e.employment_status = 'Active'
group by d.department_name, dv.division_name, j.job_title
