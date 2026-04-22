# V_MPORT_TAVLA

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates detailed mobile porting and subscription information. It retrieves data for recent orders (last 30 days) that are in a 'TIL CONSUMER' status, linking porting reports with subscriber data. It selects the most current subscription record for each main phone number based on end date and original start date, calculating various date metrics like porting year, week, and the number of days between order arrival and porting.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]

