# V_SIKKER_ROT

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies unique agreement IDs that are associated with 'Sikker ID' products (with an end date within a specific period) and also associated with 'SAFE' products (with a start date from a specific point), serving as a foundational data source for a SAFE dashboard.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
| Column Name |
|---|
| agreement_id |
| agreement_product_name |
| product_end_date |
| product_start_date |

