{{
    config(
        materialized='table'
    )
}}

with only_non_residential as (
    select *
    from  {{ ref('stg_real_estate_sale_connecticut_2008_to_2021') }}
) 

select town, 
EXTRACT(YEAR FROM sold_date) AS sale_year,
property_type,
count(property_type) as number_of_properties,
cast(avg(sale_amount) as integer) as sale_price,
non_use_code           

from only_non_residential
where property_type NOT IN ('Residential', 'Data Unavailable')
AND (EXTRACT(YEAR FROM sold_date) >= 2008 AND EXTRACT(YEAR FROM sold_date) <= 2021) 
group by 1, 3,2,6 