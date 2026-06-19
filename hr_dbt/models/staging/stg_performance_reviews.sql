with source as (
    select * from {{ ref('performance_reviews') }}
)
select
    review_id,
    employee_id,
    review_date::date     as review_date,
    reviewer_id,
    performance_score,
    goals_met_pct,
    rating_label,
    date_part('year', review_date::date) as review_year
from source
