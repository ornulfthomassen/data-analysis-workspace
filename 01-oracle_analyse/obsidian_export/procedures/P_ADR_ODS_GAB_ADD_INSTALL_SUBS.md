# P_ADR_ODS_GAB_ADD_INSTALL_SUBS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Refreshes the 'ODS_GAB_ADD_INSTALL_SUBS' table with aggregated and transformed product and address segment data. It employs a table swap mechanism involving a temporary staging table and a backup table, along with index management, statistical updates, and detailed logging of the process status and any exceptions.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_FAR_GROUP]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION_V]]
- ← [[CLM_CCM.ODS_PRODUCT_DIM]]
- ← [[CLM_FIXED_CCM.FTV_CCM_ADDRESS_SEGMENT_V]]

## Target Tables (Outputs)
- → [[ODS_GAB_ADD_INSTALL_SUBS]]
- → [[ODS_GAB_ADD_INSTALL_SUBS_N]]
- → [[ODS_GAB_ADD_INSTALL_SUBS_O]]
- → [[ODS_GAB_ADD_INSTALL_SUBS_TEMP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]

