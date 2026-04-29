# CCM_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `CCM.CCM_CUSTOMER`, acts as a direct projection or wrapper around the `CLM_CCM.CCM_CUSTOMER_V` view. It exposes a specific set of customer-related columns, serving as an intermediary data source, notably for consumption by the CCDW system (POL_KUNDEOPPLYSNINGER view). The view maintains a stable interface by selecting specific columns from its source.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| HOUSEHOLD_ID |
| CUSTOMER_STATUS_CD |
| CUSTOMER_TYPE_CD |
| DATE_OF_BIRTH |
| AGE |
| GENDER |
| FIRST_NAME |
| MIDDLE_NAME |
| SURNAME |
| RES_BRSUND_TM |
| RES_BRSUND_DM |
| RES_TELENOR_TM |
| RES_TELENOR_DM |
| ADDRESS_LINK_ID_EMAIL |
| RES_AND_APP_ID_EMAIL |
| EMAIL_IND |
| EMAIL_ADRESSE |
| EMAIL_MAX_RES_APP_DTTM |
| ADDRESS_LINK_ID_SMS |
| SMS_RES_AND_APP_ID |
| SMS_IND |
| SMS_MOBIL |
| SMS_MAX_RES_APP_DTTM |
| CREDIT_STATUS_INTERNAL_FLG |

