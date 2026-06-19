with source as (
    select * from {{ ref('divisions') }}
)
select
    division_id,
    division_name
from source
