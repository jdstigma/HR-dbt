with source as (
    select * from {{ ref('benefits_enrollment') }}
)
select
    enrollment_id,
    employee_id,
    benefit_type,
    plan_name,
    enrollment_date::date  as enrollment_date,
    monthly_cost,
    status
from source
