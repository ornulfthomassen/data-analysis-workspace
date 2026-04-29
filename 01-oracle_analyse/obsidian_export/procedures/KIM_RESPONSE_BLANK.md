# KIM_RESPONSE_BLANK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure updates specific response-related fields in the `KIM_CAMPAIGN_DETAIL_FACT` and `KIM_CUSTOMER_RESPONSE` tables, setting them to default/null-like values (-1 or 0) for records beyond a certain date threshold (August 31, 2016, and September 1, 2016, respectively). It performs these updates transactionally, first counting the rows to be affected and then verifying that the actual number of updated rows matches the count. If there's a mismatch for either update, or any other error occurs, it rolls back all changes; otherwise, it commits the changes.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_DATE_KEY |
| MEASURE_TYPE |
- ← [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| RESPONSE_DTTM |
| CONTACT_KEY |

## Target Tables (Outputs)
- → [[KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| RESPONSE_DATE_KEY |
| RESPONSE_KEY |
| RESPONSE_CHANNEL_KEY |
| RESPONSE_REASON_KEY |
| CUST_RESPONSE_KEY |
- → [[KIM_CUSTOMER_RESPONSE]]
| Column Name |
|---|
| CONTACT_KEY |
| USED_FLG |

