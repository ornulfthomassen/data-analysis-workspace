# P_CU_UPDATE_ODS_CUST_PROF_BMGM

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure updates customer agreement profile information based on filtered data from a rewards detail view. It iteratively processes records, updating specific columns in a target table, and includes logging functionality to record the execution details and number of updated rows. The procedure also dynamically creates a logging table if it doesn't already exist.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[CLM_CCM.V_ODS_AGRMT_MOB_REWARD_DET]]
| Column Name |
|---|
| AGREEMENT_ID |
| SRC_AGRM_AGREEMENT_OFFER_ID |
| KURT_ID |
| KURT_ID_AGRMT_ROLE |
| KURT_MEMBER_START_DATE |
| KURT_MEMBER_END_DATE |


## Target Tables (Outputs)
- → [[CCM.GOV_LOG_PROC_UPDATES]]
| Column Name |
|---|
| TARGET_TABLE |
| SOURCE_PROCESS |
| UPDATE_DTTM |
| ANTALL_OPPDATERT |

- → [[CLM_CCM.ODS_CUSTOMER_PROF]]
| Column Name |
|---|
| CU_AGRMT_FB_STATUS |
| CU_AGRMT_FB_START_DTTM |
| KURT_ID |


