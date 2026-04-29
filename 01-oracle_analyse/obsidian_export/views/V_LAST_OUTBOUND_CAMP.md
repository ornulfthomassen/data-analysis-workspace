# V_LAST_OUTBOUND_CAMP

**Schema:** `CCM` | **Type:** `View`

## Description
Calculates the most recent contact date-time (MAX(contact_dttm)) for each campaign code (CAMPAIGN_CD), considering only contact events that occurred within the last two days (today and yesterday).

## Data Sources (Inputs)
- ← [[cicdm.ci_cust_contact_history]]
| Column Name |
|---|
| contact_dttm |
| Cell_package_sk |
- ← [[cicdm.ci_cell_package]]
| Column Name |
|---|
| Cell_package_sk |
| CAMPAIGN_CD |

