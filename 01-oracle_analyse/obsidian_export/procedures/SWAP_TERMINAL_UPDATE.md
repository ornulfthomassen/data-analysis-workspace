# SWAP_TERMINAL_UPDATE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iterates through records in the KIM_CAMPAIGN_DETAIL_FACT_EXT table that match specific activity and campaign IDs, updating the 'PRODUCT_TP2' column to 'Terminal' for these records. It performs batch commits every 100,000 updates.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| CONTACT_KEY |
| ACTIVITY_ID |
| CAMPAIGN_ID |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| PRODUCT_TP2 |

