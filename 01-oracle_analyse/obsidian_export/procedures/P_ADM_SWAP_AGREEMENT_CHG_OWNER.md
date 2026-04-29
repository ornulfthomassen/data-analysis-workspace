# P_ADM_SWAP_AGREEMENT_CHG_OWNER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure identifies and links 'swap agreements' within the same root agreement in the `ADM_SWAP_AGREEMENT_CHG_OWNER` table. It processes two distinct matching criteria. The first criterion (C1) looks for two swap agreements under the same root where one agreement's end date exactly matches another's registration date. The second criterion (C2) looks for two swap agreements under the same root where one agreement's end date is after another's registration date, ensuring the target agreement has not already been matched. For matching pairs, it updates the `ADM_SWAP_AGREEMENT_CHG_OWNER` table with the matched agreement ID, a timestamp, matching criteria, and the number of days between the agreements' dates.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SWAP_AGREEMENT_CHG_OWNER]]
| Column Name |
|---|
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_END_DATE |
| NO_AGR_SWAP |
| MATCHED_PRODUKT_AGREEMENT_ID |
- ← [[CLM_ADM.ADM_STOCK_AGREEMENT_DEVICE_ALL]]
| Column Name |
|---|
| ROOT_AGREEMENT_KEY |
| PRODUCT_AGREEMENT_ID |
| PRODUCT_AGREEMENT_REG_DATE |
| PRODUCT_AGREEMENT_PRODUCT_KEY |
- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| DRM_COMMON_MARKET_PRODUCT |

## Target Tables (Outputs)
- → [[ADM_SWAP_AGREEMENT_CHG_OWNER]]
| Column Name |
|---|
| MATCED_DATE |
| MATCH_CRITERIA |
| MATCHED_PRODUKT_AGREEMENT_ID |
| DAYS_BETWEEN_AGREEMENTS |

