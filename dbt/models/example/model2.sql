
-- Use the `ref` function to select from other models

select timeperiod, flow1
from {{ ref('model1') }}
