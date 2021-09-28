/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

-- {{ config(materialized='table') }}

-- with sample_data as (

--     select 
--         timeperiod
--     from 10acad_sensor_data.sensor_data;
-- )

select timeperiod, flow1, occupancy1, speed1
from 10acad_sensor_data.sensor_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null