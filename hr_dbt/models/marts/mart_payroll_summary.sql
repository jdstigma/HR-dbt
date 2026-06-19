with payroll as (
    select * from {{ ref('int_payroll_enriched') }}
)

select
    pay_year,
    pay_month,
    division_name,
    department_name,
    count(distinct employee_id)             as headcount,
    round(sum(gross_pay)::numeric, 2)       as total_gross_pay,
    round(sum(net_pay)::numeric, 2)         as total_net_pay,
    round(sum(bonus)::numeric, 2)           as total_bonus,
    round(sum(overtime_pay)::numeric, 2)    as total_overtime,
    round(sum(tax_deductions)::numeric, 2)  as total_tax,
    round(avg(gross_pay)::numeric, 2)       as avg_gross_pay,
    round(avg(effective_tax_rate_pct)::numeric, 2) as avg_tax_rate_pct
from payroll
group by pay_year, pay_month, division_name, department_name
