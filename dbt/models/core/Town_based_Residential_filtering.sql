
WITH town_based_residential AS (
    SELECT
        town,
        address,
        residential_type,
        EXTRACT(YEAR FROM sold_date) AS sale_year,
        ROUND(AVG(sale_amount), 0) AS avg_sale_amount
    
       from {{ ref('stg_real_estate_sale_connecticut_2008_to_2021') }}
    WHERE
        property_type = 'Residential'
        AND EXTRACT(YEAR FROM sold_date) BETWEEN 2008 and 2021
        GROUP BY
        1,3,4,2
    ORDER BY
        1
)

SELECT
    town AS County,
    address AS Property_location,
    residential_type AS Dwelling_Type,
    sale_year AS Sale_Year,
    town_based_residential.avg_sale_amount AS Property_Type_Sale_Amount
FROM
    town_based_residential
