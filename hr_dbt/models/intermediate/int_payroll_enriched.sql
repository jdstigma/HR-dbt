with payroll as (
    select * from {{ ref('stg_payroll_history') }}
),
employees as (
    select employee_id, full_name, department_id, job_id, is_active
    from {{ ref('stg_employees') }}
),
departments as (
    select * from {{ ref('stg_departments') }}
),
divisions as (
    select * from {{ ref('stg_divisions') }}
)

select
    p.payroll_id,
    p.employee_id,
    e.full_name,
    p.pay_date,
    p.pay_year,
    p.pay_month,
    p.base_pay,
    p.bonus,
    p.overtime_pay,
    p.gross_pay,
    p.tax_deductions,
    p.benefits_deductions,
    p.net_pay,
    round((p.bonus / nullif(p.gross_pay, 0) * 100)::numeric, 2)         as bonus_pct_of_gross,
    round((p.tax_deductions / nullif(p.gross_pay, 0) * 100)::numeric, 2) as effective_tax_rate_pct,
    d.department_name,
    dv.division_name
from payroll p
left join employees   e  on p.employee_id   = e.employee_id
left join departments d  on e.department_id = d.department_id
left join divisions   dv on d.division_id   = dv.division_id
