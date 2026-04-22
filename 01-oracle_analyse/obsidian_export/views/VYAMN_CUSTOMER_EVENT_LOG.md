# VYAMN_CUSTOMER_EVENT_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `VYAMN_CUSTOMER_EVENT_LOG`, consolidates and enriches customer event data, providing a comprehensive log for analysis and reporting. It joins customer event details with event type and medium descriptions, and maps various `KURT_ID`s (for event initiator, owner, payer, and user) to anonymized `CUSTOMER_SK`s (surrogate keys) using a customer mapping table. The view includes details like subscription ID, market area, event date (with seconds handling for recent data), and hierarchical event descriptions. Its explicit purpose is stated as 'LOADING CustomerEventLog-DATA TO MJØSA', suggesting it serves as an ETL source for a data warehouse or reporting system. It filters events to approximately the last two years based on `EVENT_DATE_ID`.

## Data Sources (Inputs)
- ← [[CCDW_CUSTOMER_EVENT.CUSTOMER_EVENT_DETAIL]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_TYPE]]
- ← [[CCDW_CUSTOMER_EVENT.EVENT_MEDIUM]]
- ← [[CCDW.CUSTOMER_MAPPING]]

