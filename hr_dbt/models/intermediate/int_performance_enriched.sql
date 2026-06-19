with reviews as (
    select * from {{ ref('stg_performance_reviews') }}
),
employees as (
    select employee_id, full_name, department_id, job_id
    from {{ ref('stg_employees') }}
),
departments as (
    select * from {{ ref('stg_departments') }}
),
divisions as (
    select * from {{ ref('stg_divisions') }}
)

select
    r.review_id,
    r.employee_id,
    e.full_name,
    r.review_date,
    r.review_year,
    r.performance_score,
    r.goals_met_pct,
    r.rating_label,
    avg(r.performance_score) over (
        partition by r.employee_id
    )                                                           as employee_avg_score,
    avg(r.performance_score) over (
        partition by d.department_id, r.review_year
    )                                                           as dept_avg_score_that_year,
    d.department_name,
    dv.division_name
from reviews r
left join employees   e  on r.employee_id   = e.employee_id
left join departments d  on e.department_id = d.department_id
left join divisions   dv on d.division_id   = dv.division_id
