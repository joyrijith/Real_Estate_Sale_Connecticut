{{
    config(
        materialized='table'
    )
}}

with only_residential as (
    select *
    from {{ ref('stg_real_estate_sale_connecticut_2008_to_2021') }}
) 


select sold_date,
property_type,
residential_type,
sale_amount
from only_residential
where property_type="Residential"
AND EXTRACT(YEAR FROM sold_date) >= 2008