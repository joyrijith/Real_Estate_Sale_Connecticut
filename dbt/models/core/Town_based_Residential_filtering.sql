
WITH town_based_residential AS (
    SELECT
      *
       from {{ ref('stg_real_estate_sale_connecticut_2008_to_2021') }}

)

  select EXTRACT(YEAR FROM sold_date) AS sale_year,
           town,
           residential_type,
           count(residential_type) as number_of_properties,
           cast(avg(sale_amount) as integer) as avg_sale_price,
           non_use_code,
           count(non_use_code) as number_of_non_use_transactions

    from town_based_residential
    where (residential_type IN ('Condo' , 'Single Family', 'Two Family', 'Three Family', 'Four Family'))
    AND EXTRACT(YEAR FROM sold_date) >= 2008
    group by 1,2,3,6
   