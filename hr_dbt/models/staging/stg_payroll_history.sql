with source as (
    select * from {{ ref('payroll_history') }}
)
select
    payroll_id,
    employee_id,
    pay_date::date        as pay_date,
    base_pay,
    bonus,
    overtime_pay,
    gross_pay,
    tax_deductions,
    benefits_deductions,
    net_pay,
    date_part('year', pay_date::date)   as pay_year,
    date_part('month', pay_date::date)  as pay_month
from source
