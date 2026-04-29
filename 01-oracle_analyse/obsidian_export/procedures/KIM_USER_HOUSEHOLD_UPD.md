# KIM_USER_HOUSEHOLD_UPD

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure iterates through distinct user IDs and their associated household IDs by joining campaign detail facts with customer data. For each user ID and household ID pair retrieved, it updates the `USER_HOUSEHOLD_ID` column in the `KIM_CAMPAIGN_DETAIL_FACT` table for records matching the `KURT_ID_USER` and `MEASURE_TYPE = 1`.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_USER |
- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| KURT_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| USER_HOUSEHOLD_ID |

