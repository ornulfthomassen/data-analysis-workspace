# P_RDM_CUSTOMER_MAPPING

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_RDM_CUSTOMER_MAPPING`, is responsible for managing and maintaining a core customer mapping table (`CLM_ADM.ADM_CUSTOMER_MAPPING`) on a monthly basis. Its primary functions include:
- **Processing Customer Status Changes:** It identifies and applies changes (creations, updates, terminations, and re-creations) to customer and subscription data based on various source systems.
- **Handling Non-Customers:** It deletes or 'map-deletes' (anonymizes) records for non-customers and old personal customers (after a 2-year inactivity period).
- **Inserting New Non-Customers:** It inserts new individual and non-individual non-customer records.
- **Data Staging:** It uses an intermediate raw table (`CLM_ADM.ADM_CUSTOMER_MAPPING_RAW`) to consolidate data from multiple sources before applying changes to the main mapping table.
- **Control and Logging:** It updates a control table (`CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL`) to track the execution status of various actions and logs messages via `DBMS_OUTPUT`.
- **Data Snapshots:** It creates and manages backup, current, and historical monthly snapshots of the customer mapping data.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_CUSTOMER_INFO_KURT]]
- ← [[KURT.KURT]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HIST_KURT]]
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CLM_ADM.ADM_DEVICE_AGREEMENT_KURT]]
- ← [[ODS.CUSTOMER_ODS]]
- ← [[CLM_ADM.ADM_MONTH_DIM_V]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_UD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_RAW]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CURRENT]]
- → [[ADM_CUSTOMER_MAPPING_<YYYYMM>]]

