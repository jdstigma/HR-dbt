with source as (
    select * from {{ ref('training_records') }}
)
select
    training_id,
    employee_id,
    course_name,
    course_category,
    completion_date::date  as completion_date,
    score,
    passed,
    date_part('year', completion_date::date) as completion_year
from source
