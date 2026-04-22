# TMP_CUSTOMER_TV_V

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves customer keys and their associated 'CU_NO_TV_FTV' attribute by joining a customer information table with a customer mapping view based on a common 'KURT_ID'. It essentially maps a generic customer ID ('KURT_ID') from one table to a 'CUSTOMER_KEY' and a specific customer attribute ('CU_NO_TV_FTV').

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

