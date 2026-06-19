with source as (
    select * from {{ ref('departments') }}
)
select
    department_id,
    department_name,
    division_id,
    budget_m
from source
