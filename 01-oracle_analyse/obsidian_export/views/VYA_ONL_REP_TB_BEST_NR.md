# VYA_ONL_REP_TB_BEST_NR

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts agreement order identifiers and numerically validated sales identifiers from the 'ONL_REP.AGREEMENT_ORDER' table. It filters these records to include only those associated with the 'Telenorbutikken' sales channel, determined by joining with the 'GALAXY.DEALER_DIM' table.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
| Column Name |
|---|
| AGREEMENT_ORDER_ID |
| SALES_ID |
| DEALER_ID |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| DRM_SALES_CHANNEL_GEN03_DESC |

