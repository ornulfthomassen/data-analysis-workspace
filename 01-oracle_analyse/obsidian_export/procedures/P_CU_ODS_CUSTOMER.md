# P_CU_ODS_CUSTOMER

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_CU_ODS_CUSTOMER`) is designed to perform a full refresh (full load) of the `ODS_CUSTOMER` table. It collects core customer attributes from various source systems, filters them to identify 'persons of interest for marketing purposes' (e.g., active customers not on a communication freeze list), and then loads this processed data into a new, temporary staging table (`ODS_CUSTOMER_N`). After building indexes on this staging table, it performs a table swap operation: the existing `ODS_CUSTOMER` table is renamed to `ODS_CUSTOMER_O` (as a backup), and then `ODS_CUSTOMER_N` is renamed to `ODS_CUSTOMER`, making the newly loaded data active. The procedure includes a threshold check to ensure the number of rows in the new dataset is within an acceptable range compared to the old one before performing the swap, and it manages index renaming and grants. The overall purpose is to provide an up-to-date dataset of customer attributes for marketing and personalization.

## Data Sources (Inputs)
- ← [[ODS.CUSTOMER_ODS]]
- ← [[ODS.CUSTOMER_RES_AND_APP]]
- ← [[CLM_CCM.ODS_CUSTOMER_COMM_FREEZE]]
- ← [[CCDW.CUSTOMER]]
- ← [[ALL_INDEXES]]

## Target Tables (Outputs)
- → [[ODS_CUSTOMER]]
- → [[ODS_CUSTOMER_N]]
- → [[ODS_CUSTOMER_O]]

