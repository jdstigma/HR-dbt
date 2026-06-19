with source as (
    select * from {{ ref('attendance_summary') }}
)
select
    attendance_id,
    employee_id,
    year,
    month,
    working_days,
    days_present,
    days_absent,
    days_wfh,
    overtime_hours,
    round(days_present::numeric / nullif(working_days, 0) * 100, 2) as attendance_rate_pct
from source
