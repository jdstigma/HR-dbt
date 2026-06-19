with source as (
    select * from {{ ref('jobs') }}
)
select
    job_id,
    job_title,
    job_family,
    level,
    min_salary,
    max_salary,
    max_salary - min_salary as salary_band_range
from source
