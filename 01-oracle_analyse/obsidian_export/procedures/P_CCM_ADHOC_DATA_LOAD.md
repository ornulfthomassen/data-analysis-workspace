# P_CCM_ADHOC_DATA_LOAD

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure manages the loading of ad-hoc customer campaign data from dynamically specified source tables into a central ad-hoc data table. It performs several validation checks, including ensuring a single campaign code per source table and preventing duplicate campaign codes in the target. It updates a control table with the status and details of each load operation, and logs errors/warnings to a load history table.

## Data Sources (Inputs)
- ← [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]
| Column Name |
|---|
| LOAD_STATUS |
| ADHOC_TABLE |
| END_DATE |
- ← [[ADHOC_CMD.[DYNAMIC_SOURCE_TABLE]]]
| Column Name |
|---|
| KURT_ID |
| SUBSCRIPTION_ID |
| K2_PUID |
| CAMPAIGN_CODE |
| DESCRIPTION |
| ADDRESS_EMAIL_NAME |
| NUMERIC_FIELD_1 |
| NUMERIC_FIELD_2 |
| NUMERIC_FIELD_3 |
| NUMERIC_FIELD_4 |
| NUMERIC_FIELD_5 |
| NUMERIC_FIELD_6 |
| NUMERIC_FIELD_7 |
| NUMERIC_FIELD_8 |
| NUMERIC_FIELD_9 |
| CHARACTER_FIELD_1 |
| CHARACTER_FIELD_2 |
| CHARACTER_FIELD_3 |
| CHARACTER_FIELD_4 |
| CHARACTER_FIELD_5 |
| CHARACTER_FIELD_6 |
| CHARACTER_FIELD_7 |
| CHARACTER_FIELD_8 |
| CHARACTER_FIELD_9 |
| DATE_FIELD_1 |
| DATE_FIELD_2 |
| DATE_FIELD_3 |
| DATE_FIELD_4 |
| DATE_FIELD_5 |
| DATE_FIELD_6 |
| DATE_FIELD_7 |
| DATE_FIELD_8 |
| DATE_FIELD_9 |
- ← [[CLM_CCM.CCM_ADHOC_DATA]]
| Column Name |
|---|
| CAMPAIGN_CODE |

## Target Tables (Outputs)
- → [[ADHOC_CMD.ADHOC_CONTROL_SASCI]]
| Column Name |
|---|
| ADHOC_TABLE |
| LOAD_DESTINATION |
| LOAD_STATUS |
| LOAD_DATE |
| CAMPAIGN_CODE |
| DESCRIPTION |
- → [[CLM_CCM.CCM_ADHOC_DATA]]
| Column Name |
|---|
| KURT_ID |
| SUBSCRIPTION_ID |
| K2_PUID |
| CAMPAIGN_CODE |
| DESCRIPTION |
| END_DATE |
| LOAD_DATE |
| ADHOC_TABLE |
| ADDRESS_EMAIL_NAME |
| NUMERIC_FIELD_1 |
| NUMERIC_FIELD_2 |
| NUMERIC_FIELD_3 |
| NUMERIC_FIELD_4 |
| NUMERIC_FIELD_5 |
| NUMERIC_FIELD_6 |
| NUMERIC_FIELD_7 |
| NUMERIC_FIELD_8 |
| NUMERIC_FIELD_9 |
| CHARACTER_FIELD_1 |
| CHARACTER_FIELD_2 |
| CHARACTER_FIELD_3 |
| CHARACTER_FIELD_4 |
| CHARACTER_FIELD_5 |
| CHARACTER_FIELD_6 |
| CHARACTER_FIELD_7 |
| CHARACTER_FIELD_8 |
| CHARACTER_FIELD_9 |
| DATE_FIELD_1 |
| DATE_FIELD_2 |
| DATE_FIELD_3 |
| DATE_FIELD_4 |
| DATE_FIELD_5 |
| DATE_FIELD_6 |
| DATE_FIELD_7 |
| DATE_FIELD_8 |
| DATE_FIELD_9 |
- → [[CLM_CCM.CCM_LOAD_HISTORY]]

