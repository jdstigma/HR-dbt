with source as (
    select * from {{ ref('employees') }}
)

select
    employee_id,
    first_name,
    last_name,
    first_name || ' ' || last_name   as full_name,
    email,
    gender,
    ethnicity,
    birth_date::date                  as birth_date,
    hire_date::date                   as hire_date,
    termination_date::date            as termination_date,
    employment_status,
    employment_type,
    department_id,
    job_id,
    location_id,
    salary,
    manager_id,
    case
        when termination_date is null then true
        else false
    end                               as is_active
from source
