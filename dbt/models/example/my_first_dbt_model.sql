/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with sample_data as (

    select * from sensors.sensor_data where id < 5
)

select *
from sensors.sensor_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null