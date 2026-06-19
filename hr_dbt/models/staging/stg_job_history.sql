with source as (
    select * from {{ ref('job_history') }}
)
select
    history_id,
    employee_id,
    job_id,
    department_id,
    location_id,
    salary,
    start_date::date                         as start_date,
    nullif(end_date::text, '')::date         as end_date,
    change_reason
from source
