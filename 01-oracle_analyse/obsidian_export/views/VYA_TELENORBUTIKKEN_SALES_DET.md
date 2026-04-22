# VYA_TELENORBUTIKKEN_SALES_DET

**Schema:** `CCM` | **Type:** `View`

## Description
Provides anonymized and enriched detailed sales transaction records from 'Telenorbutikken' for loading into Viya. It enriches sales with a three-level product group hierarchy, anonymizes seller names if no sales activity is recorded within the last 365 days, anonymizes 'unknown' customer names, and links sales to historical clerk and customer subscription master data based on the transaction date.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.T_BUTIKKEN_DEVICES]]
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]

