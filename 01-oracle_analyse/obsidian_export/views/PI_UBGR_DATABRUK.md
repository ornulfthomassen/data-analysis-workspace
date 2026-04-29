# PI_UBGR_DATABRUK

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a view named PI_UBGR_DATABRUK to expose specific data usage information for unlimited subscriptions, primarily by selecting all columns from the ad-hoc result table adhoc_bs.ah_2430_res. The view acts as a direct projection of this source table, renaming columns if necessary to match the view's defined column names.

## Data Sources (Inputs)
- ← [[adhoc_bs.ah_2430_res]]
| Column Name |
|---|
| period_id |
| subscription_sk |
| prim_start_date |
| prim_end_date |
| poid |
| prim_product_desc |
| gb_data_tot |
| gb_data_main |
| gb_data_sub |
| sub_flag |
| numb_numb_used |

