# P_ADM_CUSTOMER_USE_USER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure processes and aggregates monthly customer usage and subscription data. It constructs a temporary staging table by joining various customer and subscription aggregation sources, then efficiently loads this aggregated data into a specific partition of the permanent target table 'CLM_ADM.ADM_CUSTOMER_USE_USER' using an 'ALTER TABLE EXCHANGE PARTITION' operation. The procedure also handles the creation of new partitions in the target table if they don't exist for the given month and collects statistics on the newly loaded partition.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CRM_ANALYSE.ADM_KURT_USER_SUBS_AGG]]

## Target Tables (Outputs)
- → [[CLM_ADM.TMP_CUSTOMER_USE_USER]]
- → [[CLM_ADM.ADM_CUSTOMER_USE_USER]]

