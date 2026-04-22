# ADM18_2_CUSTOMER_USER_DET_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `ADM18_2_CUSTOMER_USER_DET_HIST` is designed to create and populate a historical, partitioned table named `CRM_ANALYSE.ADM_CUSTOMER_USER_DETAIL_HIST`. It processes customer subscription and usage data on a monthly basis. For a specified range of months (or the previous month if no range is provided), it aggregates various metrics related to mobile subscriptions, main number associations (like BankID), and social network analysis (SNA) metrics for both postpaid and prepaid mobile services. The procedure dynamically checks for the existence of the target table and its monthly partitions, creating them if they don't exist. It then inserts the newly aggregated data for each relevant month, performing a commit and gathering statistics after each monthly insertion. It also includes logging mechanisms for process status and errors.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_AGG]]
- ← [[CRM_ANALYSE.ADM_MAIN_NUMBER_BANKID]]
- ← [[CCDW_CONSUMERANALYSE.CON_SNA_AGG]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_CUSTOMER_USER_DETAIL_HIST]]

