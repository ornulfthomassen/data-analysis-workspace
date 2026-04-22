# VYA_ODS_OTT_MIN_SKY_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and presents current usage statistics for the 'Min Sky' OTT service. It calculates various metrics at a customer level, including creation and last activity dates, sums of foreground and connection events over the last 7, 30, and 180 days, total and used storage quota, media file count, and opt-out status for product improvement analytics. The purpose is to provide a summary of application usage linked to customer identifiers, likely for reporting or data warehousing (as indicated by 'Loading APP-usage to Mjøsa').

## Data Sources (Inputs)
- ← [[CLM_ADM.SCD2_MIN_SKY_MAIN]]
- ← [[ODS.CONNECT_ID_LINK]]
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]

