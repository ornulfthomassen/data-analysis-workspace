# GCP_SUBSCRIPTION_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
View providing events on subscription level, used by CI MA to generate salestips, with a filter to remove specific events (ID 32, speed reduction) that did not occur in the current month.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION_EVENTS]]
| Column Name |
|---|
| EVENT_ID |
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| KURT_ID |
| EVENT_NM |
| EVENT_DETAIL |
| EVENT_DTTM |
| EVENT_DETECTION_DTTM |
| EVENT_VALID_TO_DTTM |
| EVENT_VALUE_1_DESC |
| EVENT_VALUE_1 |
| EVENT_VALUE_2_DESC |
| EVENT_VALUE_2 |
| EVENT_VALUE_3_DESC |
| EVENT_VALUE_3 |
| EVENT_VALUE_4_DESC |
| EVENT_VALUE_4 |
| EVENT_VALUE_NUM_1 |
| EVENT_VALUE_NUM_1_DESC |
| EVENT_VALUE_NUM_2 |
| EVENT_VALUE_NUM_2_DESC |
| EVENT_VALUE_NUM_3 |
| EVENT_VALUE_NUM_3_DESC |
| EVENT_VALUE_NUM_4 |
| EVENT_VALUE_NUM_4_DESC |
| EVENT_VALUE_NUM_5 |
| EVENT_VALUE_NUM_5_DESC |
| EVENT_VALUE_NUM_6 |
| EVENT_VALUE_NUM_6_DESC |

