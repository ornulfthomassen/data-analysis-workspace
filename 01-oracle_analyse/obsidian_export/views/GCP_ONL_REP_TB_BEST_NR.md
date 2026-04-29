# GCP_ONL_REP_TB_BEST_NR

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts agreement order IDs and sales numbers from the ONL_REP.AGREEMENT_ORDER table. It filters these orders to include only those associated with 'Telenorbutikken' sales channels and for which the sales ID is a valid number, and the order arrival date is within the last three years from the current date. It renames the output columns to AGREEMENT_SOURCE_ORDER_ID and BESTILLINGSNUMMER.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| SALES_ID |
| DEALER_ID |
| ORDER_ARRIVAL_DATE |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| DRM_SALES_CHANNEL_GEN03_DESC |

