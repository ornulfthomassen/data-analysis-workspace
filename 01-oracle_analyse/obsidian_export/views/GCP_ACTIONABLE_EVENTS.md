# GCP_ACTIONABLE_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides event data for customer interactions, primarily for CLM (Customer Lifecycle Management) activities, transferring data from RTDM to SAS360. It is also used to define subject-level customers in an infomap. It filters events based on `PROCCESED_DTTM` and `INPUTS_TRIGGERID`, and transforms various input fields into a standardized event format.

## Data Sources (Inputs)
- ← [[CLM_RTDM.ESP_TRIGGER_HISTORY]]
| Column Name |
|---|
| INPUTS_TRIGGERID |
| SOURCESYSTEM |
| INPUTS_ESPKURTID |
| INPUTS_ESPSUBSCRIPTIONID |
| INPUTS_NUMDATA2 |
| INPUTS_SUBSCRIPTIONROLE |
| INPUTS_ESPMAINNUMBER |
| PROCCESED_DTTM |
| INPUTS_DATEDATA1 |
| INPUTS_NUMDATA1 |
| INPUTS_CHARDATA1 |
| INPUTS_NUMDATA4 |
| INPUTS_NUMDATA3 |
| INPUTS_CHARDATA2 |
| INPUTS_CHARDATA4 |
| INPUTS_CHARDATA5 |
| INPUTS_CHARDATA6 |
| INPUTS_DATEDATA2 |

