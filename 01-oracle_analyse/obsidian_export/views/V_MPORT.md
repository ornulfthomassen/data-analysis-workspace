# V_MPORT

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates information related to mobile number porting events. It combines subscription details, porting order data, and profit segment categorization. It calculates various date-related metrics for porting, such as porting date, year, week, and the number of days between order arrival and porting. The view provides a comprehensive dataset for analyzing mobile number porting activities, linking specific subscriptions to their porting orders and associated profit categories.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
- ← [[PROFIT.CP_CAT_BED_PRIV]]

