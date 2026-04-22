# P_ADM_SUBSCRIPTION_HIST_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure P_ADM_SUBSCRIPTION_HIST_KURT computes and stores monthly subscription historical data for a specified period (V_YYYYMM). It manages the main output table 'ADM_SUBSCRIPTION_HIST_KURT' by renaming the existing one as a backup ('_OLD') and dropping older backup versions. It then creates two intermediate temporary tables ('TMP1_SUBSCRIPTION_HIST_KURT' and 'TMP2_SUBSCRIPTION_HIST_KURT') by extracting, transforming, and cleaning data from various source systems related to subscriptions, products, and dates. Finally, it populates the new 'ADM_SUBSCRIPTION_HIST_KURT' table by joining the temporary tables and calculating various subscription-related metrics such as days active, days since last change, and binding period details. The procedure also creates indexes, gathers statistics on the newly created tables, and includes robust error handling and logging.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]

## Target Tables (Outputs)
- → [[ADM_SUBSCRIPTION_HIST_KURT]]
- → [[ADM_SUBSCRIPTION_HIST_KURT_OLD]]
- → [[TMP1_SUBSCRIPTION_HIST_KURT]]
- → [[TMP2_SUBSCRIPTION_HIST_KURT]]

