with performance as (
    select * from {{ ref('int_performance_enriched') }}
)

select
    review_year,
    division_name,
    department_name,
    count(distinct employee_id)                         as employees_reviewed,
    round(avg(performance_score)::numeric, 2)           as avg_performance_score,
    round(avg(goals_met_pct)::numeric, 2)               as avg_goals_met_pct,
    sum(case when rating_label = 'Exceptional'          then 1 else 0 end) as exceptional,
    sum(case when rating_label = 'Exceeds Expectations' then 1 else 0 end) as exceeds_expectations,
    sum(case when rating_label = 'Meets Expectations'   then 1 else 0 end) as meets_expectations,
    sum(case when rating_label = 'Below Expectations'   then 1 else 0 end) as below_expectations,
    sum(case when rating_label = 'Unsatisfactory'       then 1 else 0 end) as unsatisfactory
from performance
group by review_year, division_name, department_name
