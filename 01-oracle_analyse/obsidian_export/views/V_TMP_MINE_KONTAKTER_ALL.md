# V_TMP_MINE_KONTAKTER_ALL

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates user/contact activity and subscription details, enriching it with product and customer information. It calculates duration metrics such as 'days used' (time between creation and last sync) and 'days since last sync', providing a comprehensive dataset for CRM or customer behavior analysis.

## Data Sources (Inputs)
- ← [[TMP_MINE_KONTAKTER_ALL]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]

