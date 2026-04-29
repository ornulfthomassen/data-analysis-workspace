# CM_MOB_SP

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Consolidates mobile subscription details, including associated products, components, and hierarchical product catalog information, by joining data from various operational and catalog systems, filtered for active records and specific source systems.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| DIRECTORY_NUMBER_ID |
| SUBSCR_ID |
| INFO_IS_DELETED |
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_OFFER_INC_ID |
| SUBSCR_ID |
| PRODUCT_OFFER_ID |
| PARAMETER_ID |
| INC_VALID_FROM_DATE |
| INC_VALID_TO_DATE |
| INFO_REG_DATE |
| INFO_REG_APPL_NAME |
| INFO_REG_USER_NAME |
| INFO_CHG_DATE |
| INFO_CHG_APPL_NAME |
| INFO_CHG_USER_NAME |
| INFO_IS_DELETED |
| ORIGINAL_FROM_DATE |
| ORIGINAL_END_DATE |
| SUBSCRIBED_OFFER_ID |
| STATUS |
| AGREEMENT_MEMBER_ID |
| SUBSCRIBED_COMPONENT_ID |
- ← [[PCAT.COMPONENT]]
| Column Name |
|---|
| NAME |
| COMPONENT_ID |
- ← [[GPD]]
| Column Name |
|---|
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| SOURCE_SYSTEM_NAME |
| PRODUCT_KEY |
- ← [[PTC]]
| Column Name |
|---|
| PARENT |
| ID |
| H_LEVEL |
| DESCRIPTION |

