# TMP_CUSTOMER_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a temporary view of customer status information by selecting, transforming, and filtering data from the ADM_CUSTOMER_INFO_HIST table. It maps customer status codes to Norwegian descriptions and excludes specific customer records, with the explicit purpose of loading this data into Viya.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| CUSTOMER_SK |
| CUSTOMER_STATUS_CD |
| CUSTOMER_TYPE_CD |

