with employees as (
    select * from {{ ref('int_employees_enriched') }}
)

select
    date_part('year', termination_date)::int    as termination_year,
    division_name,
    department_name,
    job_family,
    level,
    region,
    employment_type,
    count(*)                                    as terminations,
    round(avg(tenure_years)::numeric, 1)        as avg_tenure_at_exit_years,
    round(avg(salary)::numeric, 2)              as avg_salary_at_exit
from employees
where is_active = false
  and termination_date is not null
group by
    date_part('year', termination_date),
    division_name, department_name,
    job_family, level, region, employment_type
