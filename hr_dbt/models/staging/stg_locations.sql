with source as (
    select * from {{ ref('locations') }}
)
select
    location_id,
    city,
    state,
    country,
    region,
    office_type
from source
