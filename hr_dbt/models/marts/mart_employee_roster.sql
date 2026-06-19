with enriched as (
    select * from {{ ref('int_employees_enriched') }}
)

select
    employee_id,
    full_name,
    email,
    gender,
    ethnicity,
    age_years,
    hire_date,
    termination_date,
    tenure_years,
    employment_status,
    employment_type,
    is_active,
    department_name,
    division_name,
    job_title,
    job_family,
    level,
    salary,
    min_salary,
    max_salary,
    salary_position_in_band_pct,
    city,
    state,
    country,
    region,
    office_type
from enriched
