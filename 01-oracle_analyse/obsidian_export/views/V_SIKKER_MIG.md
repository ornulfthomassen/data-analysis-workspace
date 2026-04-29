# V_SIKKER_MIG

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies distinct agreement IDs that meet two sets of criteria from the `clm_ccm.v_ods_agrmt_offer_mob_safety` view. Specifically, it retrieves agreement IDs that are associated with 'Sikker ID' products having an end date between March 23, 2020, and the day after the current date, AND are also associated with 'SAFE' products having a start date on or after March 23, 2020.

## Data Sources (Inputs)
- ← [[clm_ccm.v_ods_agrmt_offer_mob_safety]]
| Column Name |
|---|
| agreement_id |
| agreement_product_name |
| product_end_date |
| product_start_date |

