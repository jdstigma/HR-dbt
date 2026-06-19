{{ config(materialized='table') }}

with base as (
    select
        e.employee_id,
        e.salary,
        e.department_id,
        d.department_name,
        dv.division_name,
        date_part('year', age(current_date, e.hire_date))  as tenure_years,
        ln(e.salary)                                        as ln_salary
    from {{ ref('stg_employees') }} e
    join {{ ref('stg_departments') }} d  using (department_id)
    join {{ ref('stg_divisions') }}  dv using (division_id)
    where e.employment_status = 'Active'
      and e.salary > 0
),

global_reg as (
    select
        'All Employees'                                        as scope,
        count(*)                                               as n,
        round(regr_slope(salary, tenure_years)::numeric, 2)   as salary_per_year,
        round(regr_intercept(salary, tenure_years)::numeric, 2) as base_salary,
        round(regr_r2(salary, tenure_years)::numeric, 4)      as r_squared,
        round(corr(salary, tenure_years)::numeric, 4)         as correlation,
        round(regr_slope(ln_salary, tenure_years)::numeric, 4) as log_slope,
        round(regr_r2(ln_salary, tenure_years)::numeric, 4)   as log_r_squared
    from base
),

div_reg as (
    select
        division_name                                          as scope,
        count(*)                                               as n,
        round(regr_slope(salary, tenure_years)::numeric, 2)   as salary_per_year,
        round(regr_intercept(salary, tenure_years)::numeric, 2) as base_salary,
        round(regr_r2(salary, tenure_years)::numeric, 4)      as r_squared,
        round(corr(salary, tenure_years)::numeric, 4)         as correlation,
        round(regr_slope(ln_salary, tenure_years)::numeric, 4) as log_slope,
        round(regr_r2(ln_salary, tenure_years)::numeric, 4)   as log_r_squared
    from base
    group by division_name
)

select * from global_reg
union all
select * from div_reg
order by scope
