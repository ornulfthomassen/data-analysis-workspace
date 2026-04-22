# V_AST_RESPONSE

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and categorizes responses to sales tips, providing an analytical perspective on their type (e.g., Newsale, Upsale), status (Accepted/Rejected), and associated customer/subscription information over time. It specifically sums the response quantity for records where no explicit contact quantity was recorded (CONTACTED_QUANTITY = 0), suggesting a focus on unsolicited or passively received responses.

## Data Sources (Inputs)
- ← [[GALAXY.SALESTIPS_DETAIL_FACT_V]]
- ← [[GALAXY.SALESTIPS_RESPONSE_DT_DIM_V]]
- ← [[GALAXY.SALESTIPS_RESPONSE_DIM_V]]
- ← [[GALAXY.SALESTIPS_DIM_V]]

