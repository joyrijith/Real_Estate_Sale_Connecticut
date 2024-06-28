
{{
    config(
        materialized='view'
    )
}}

with 

source as (
    select * ,
    row_number() over(partition by Serial_Number, date_recorded) as rn  
   from {{ source('staging', 'real_estate_sale_connecticut_2008_to_2021') }}

)


    select
        {{dbt_utils.generate_surrogate_key(['Serial_Number','date_recorded'])}} as Serial_Number,
        list_year,
        PARSE_DATE('%m/%d/%Y', date_recorded) as sold_date,
        cast(town as string) as town,
        cast(address as string) as address,
        cast(assessed_value as integer) as assessed_value,
        cast(sale_amount as integer) as sale_amount,
        safe_cast(sold_to_assessed_percentage as numeric) as sold_to_assessed_percentage,
        cast(Property_type as string) as property_type,
        cast(residential_type as string) as residential_type,
        cast(non_use_code as string) as non_use_code
    from source
    where rn = 1
