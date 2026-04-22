# P_GDPR_POINT_DELETE_ANALYSE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_GDPR_POINT_DELETE_ANALYSE` is designed to analyze and process GDPR (General Data Protection Regulation) point deletion requests for customers. Its main functions include:
1.  **Backup Customer Data**: It creates a backup of relevant customer mapping information into a dedicated backup table.
2.  **Identify Customers for Action**: It identifies specific customer records (both 'ex-customers' and 'non-customers') that are due for GDPR point deletion or reporting based on criteria from an analysis view.
3.  **Log and Control Actions**: It meticulously logs the status and progress of these actions in a control table.
4.  **Orchestrate Point Deletion**: For identified customers, it invokes an external procedure (`CCDW.P_GDPR_POINT_DELETED`) to perform the actual 'point deletion' or update the deletion status in a source table (though the direct update statements within this procedure are commented out in the provided script).
5.  **Monitor Request Status**: It checks for and flags any overdue or unhandled GDPR deletion requests, raising errors if such anomalies are detected.
6.  **Error Handling and Logging**: It incorporates comprehensive error handling mechanisms and logs all significant events and errors using a history logging procedure.

## Data Sources (Inputs)
- ← [[CCDW.GDPR_POINT_DEL_ANALYSE_V]]
- ← [[CCDW.CUSTOMER_MAPPING]]
- ← [[CCDW.GDPR_POINT_DELETION]]
- ← [[ODS.AGREEMENT_ODS_MOB]]
- ← [[PD]]
- ← [[ODS.AGREEMENT_OFFER_ODS_MOB]]
- ← [[ODS.SUBSCRIPTION_ODS_FIXED]]
- ← [[ODS.SUBSCRIPTION_ODS_FTV]]
- ← [[ODS.SUBSCRIPTION_ODS_MOB]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP_PD]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BACKUP_PD]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_BCK_PD_OK]]
- → [[CLM_ADM.ADM_CUSTOMER_MAPPING_CTRL_PD]]
- → [[CRM_ANALYSE.ADM_LOAD_HISTORY]]

