# VYA_ODS_AGRMT_OFFER_MOB_RW_DT

**Schema:** `CCM` | **Type:** `View`

## Description
The view prepares and enriches agreement offer mobile reward detail data. It joins agreement reward details with customer mapping information to identify both the owner and member customer keys (SKs), likely for loading this transformed data into a data warehouse or another system.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_MOB_REWARD_DET]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| AGREEMENT_END_DATE |
| KURT_ID_AGRMT_OWNER_VS_MEMBER |
| KURT_MEMBER_START_DATE |
| KURT_MEMBER_END_DATE |
| UNIT_PRODUCT_KEY |
| UNIT_PRODUCT_NAME |
| UNIT_CCDW_KEY |
| UNIT_TYPE |
| UNIT_SOURCE_SYSTEM_ID |
| UNIT_REWARD_BASIS |
| UNIT_REWARD_CAN_USE |
| KURT_ID_OWNER_AGREEMENT |
| KURT_ID_MEMBER |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| CUSTOMER_SK |
| KURT_ID |

