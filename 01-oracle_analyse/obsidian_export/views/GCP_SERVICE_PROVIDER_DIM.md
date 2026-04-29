# GCP_SERVICE_PROVIDER_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms and combines service provider details from the `CCDW.SERVICE_PROVIDER` table with group information from `CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM` to create a consolidated service provider dimension view. This includes data cleaning (e.g., service provider names), type casting (e.g., service provider surrogate key), and date handling for effective and end dates, preparing the data for dimensional modeling or loading into a data warehouse.

## Data Sources (Inputs)
- ← [[CCDW.SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| SERVICE_PROVIDER_NAME |
| NETWORK_PROVIDER_ID |
| HAS_NETWORK |
| SOURCE_SERVICE_PROVIDER_ID |
| START_DATE |
| END_DATE |
| INFO_REG_DATE |
- ← [[CRM_ANALYSE.ADM_SERVICE_PROVIDER_DIM]]
| Column Name |
|---|
| SERVICE_PROVIDER_GROUP |
| SERVICE_PROVIDER_KEY |

