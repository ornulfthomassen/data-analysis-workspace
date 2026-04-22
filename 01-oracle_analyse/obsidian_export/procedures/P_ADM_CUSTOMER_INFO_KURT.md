# P_ADM_CUSTOMER_INFO_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_CUSTOMER_INFO_KURT`, performs a monthly refresh of a comprehensive customer information table named `ADM_CUSTOMER_INFO_KURT`. It compiles data for the previous month (determined by `V_YYYYMM`) from various operational and data warehouse sources, including customer demographics, contact details, household information, and address attributes. The procedure first validates the availability of data in its source tables. Subsequently, it manages table versions by renaming the existing `ADM_CUSTOMER_INFO_KURT` table to `ADM_CUSTOMER_INFO_KURT_OLD` (acting as a backup) and then creates a new `ADM_CUSTOMER_INFO_KURT` table with the latest refreshed data. It also includes logic to drop old backup tables under specific conditions and gathers statistics on the newly created table for performance optimization.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CLM_CCM.CCM_CUST_CONTACT_ADDRESS_V]]
- ← [[ODS.CUSTOMER_ODS]]
- ← [[CCDW.CUSTOMER]]
- ← [[ODS.CUSTOMER_RES_AND_APP]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO_V]]
- ← [[CLM_CCM.CCM_FAR_V]]
- ← [[CCDW.ADDRESS_TYPE]]
- ← [[CCDW.ADDRESS_STATUS]]
- ← [[ADM_CUSTOMER_INFO_KURT_OLD]]

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_INFO_KURT]]
- → [[ADM_CUSTOMER_INFO_KURT_OLD]]

