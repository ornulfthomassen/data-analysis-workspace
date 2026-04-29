# VYA_CM_SUBSCRIPTION_SIMCARD_TYPE

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named `VYA_CM_SUBSCRIPTION_SIMCARD_TYPE`, consolidates and transforms subscription and SIM card type data from various source systems. Its primary purpose, as indicated by comments, is to prepare this data for loading into a target system called MJØSA. It integrates SIM card details, product dimensions, and subscription mapping information, applying complex logic for handling historical validity dates (using `LAG` analytic function), filtering out specific product offers, deriving SIM card numbers based on card type, and de-duplicating SIM card details.

## Data Sources (Inputs)
- ← [[SIMNR.SIMCARD_DETAILS]]
| Column Name |
|---|
| ICC_ID |
| IMSI_NUMBER |
- ← [[CM.REL_NUMBER]]
| Column Name |
|---|
| PRODUCT_OFFER_ID |
| SUBSCRIBED_OFFER_ID |
| VALID_TO_DATE |
| VALID_FROM_DATE |
| SUBSCRIPTION_SIMCARD_TYPE |
| MSISDN |
| ICC_ID |
| ACTIVATION_PARAMETER_ID |
| SUBSCR_ID_OWNER |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SUBSCRIPTION_ID |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_KEY |
- ← [[CM.SUBSCRIPTION_EQUIPMENT_INFO]]
| Column Name |
|---|
| SUBSCR_ID |
| INFO_IS_DELETED |
| VALID_TO_DATE |
| ICC_ID |
| VALID_FROM_DATE |
| IMSI_NUMBER_ID |

