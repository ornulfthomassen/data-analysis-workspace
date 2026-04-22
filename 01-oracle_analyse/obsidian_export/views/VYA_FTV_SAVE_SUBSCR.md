# VYA_FTV_SAVE_SUBSCR

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and enriches detailed information about customer churn cases, particularly focusing on 'saved' churn instances. It combines core churn case attributes (such as reason, solution, dates, origin, channels, and product descriptions) with associated customer and location subscription keys (broadband and TV), customer master data, and time-based dimensions (year-week of churn creation). Its purpose is to provide a comprehensive dataset for analyzing churn prevention efforts and understanding the characteristics of saved churn cases.

## Data Sources (Inputs)
- ← [[CCM.VYA_FTV_CVIEW_SAVE]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CCM.VYA_FTV_KAS_CUST_SUB_KEY]]
- ← [[CCM.VYA_FTV_KAS_LOC_SUB_KEY]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

