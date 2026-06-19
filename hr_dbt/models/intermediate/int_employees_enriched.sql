with employees as (
    select * from {{ ref('stg_employees') }}
),
departments as (
    select * from {{ ref('stg_departments') }}
),
divisions as (
    select * from {{ ref('stg_divisions') }}
),
jobs as (
    select * from {{ ref('stg_jobs') }}
),
locations as (
    select * from {{ ref('stg_locations') }}
)

select
    e.employee_id,
    e.full_name,
    e.email,
    e.gender,
    e.ethnicity,
    e.birth_date,
    e.hire_date,
    e.termination_date,
    e.employment_status,
    e.employment_type,
    e.salary,
    e.manager_id,
    e.is_active,
    date_part('year', age(current_date, e.hire_date))   as tenure_years,
    date_part('year', age(current_date, e.birth_date))  as age_years,
    d.department_name,
    dv.division_name,
    j.job_title,
    j.job_family,
    j.level,
    j.min_salary,
    j.max_salary,
    round((e.salary - j.min_salary)::numeric / nullif(j.max_salary - j.min_salary, 0) * 100, 2) as salary_position_in_band_pct,
    l.city,
    l.state,
    l.country,
    l.region,
    l.office_type
from employees e
left join departments d  on e.department_id  = d.department_id
left join divisions  dv on d.division_id     = dv.division_id
left join jobs       j  on e.job_id          = j.job_id
left join locations  l  on e.location_id     = l.location_id
