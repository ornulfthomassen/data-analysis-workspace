# P_ADM_AGREEMENT_DEVICE_TRANSFR

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Populates and updates the `ADM_AGREEMENT_DEVICE_TRANSFER` table. It first inserts new device agreement transfer records from `ADM_AGREEMENT_DEVICE_ALL` that meet specific criteria, calculates an initial transfer rank, and then iteratively updates existing records in `ADM_AGREEMENT_DEVICE_TRANSFER` by linking sequential device agreements for the same IMEI. This linking process identifies 'first' and 'next' agreements, populating matching criteria and related agreement details.

## Data Sources (Inputs)
- ← [[ADM_AGREEMENT_DEVICE_TRANSFER]]
| Column Name |
|---|
| PRODUCT_AGREEMENT_END_DATE |
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| IMEI |
| TRANSFERE_RANK |
| DEVICE_AGREEMENT_START_DATE |
| DEVICE_AGREEMENT_END_DATE |
| DEVICE_AGREEMENT_ID |
| ORDER_CUSTOMER_SK_OWNER |
| MATCH_IMEI |
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_ALL]]
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_MARKET_PRODUCT |
- ← [[CLM_ADM.ADM_AGREEMENT_DEVICE_AGG_V]]
| Column Name |
|---|
| DEV_AGREEMENT_KEY |

## Target Tables (Outputs)
- → [[ADM_AGREEMENT_DEVICE_TRANSFER]]
| Column Name |
|---|
| MATCHED_DATE |
| MATCH_CRITERIA |
| MATCH_IMEI |
| FIRST_DAYS_BETWEEN_AGREEMENTS |
| NEXT_DAYS_BETWEEN_AGREEMENTS |
| FIRST_START_DATE |
| NEXT_START_DATE |
| FIRST_END_DATE |
| NEXT_END_DATE |
| FIRST_ROOT_AGREEMENT_KEY |
| NEXT_ROOT_AGREEMENT_KEY |
| FIRST_PRODUKT_AGREEMENT_ID |
| NEXT_PRODUKT_AGREEMENT_ID |
| FIRST_DEVICE_AGREEMENT_ID |
| NEXT_DEVICE_AGREEMENT_ID |
| FIRST_OWNER_SK |
| NEXT_OWNER_SK |
| TRANSFERE_RANK |

