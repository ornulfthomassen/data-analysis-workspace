# V_ANALYTICAL_MASTER_TABLE_HH

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_ANALYTICAL_MASTER_TABLE_HH, generates a comprehensive monthly analytical dataset at the household level. It consolidates various household attributes including demographics (age, gender), contact preferences, geographical information, and detailed statistics on various telecommunications services. These service statistics cover mobile (postpaid, prepaid, broadband), fixed-line, DSL, and fiber, detailing subscription counts, user counts, net revenue, and extensive usage metrics (data, SMS, MMS, voice calls, activity days) over recent months. It also includes information on broadband coverage and speed capabilities for the household's address.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_INFO_HIST]]
- ← [[CLM_ADM.ADM_HH_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_HOUSEHOLD_SUBS_CNT]]
- ← [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]

