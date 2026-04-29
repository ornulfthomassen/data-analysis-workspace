# P_HH_SCORE_CCM_CUSTOMER_CLM_SEGM

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Predicts the presence of children in households and derives customer life stage segments based on customer age and household demographic data. It updates the permanent target table CLM_CCM.CCM_CUSTOMER_CLM_SEGMENT by creating a new temporary version, comparing row counts against a threshold, and then performing a table swap (rename) while backing up the old version. It also logs the execution status to a history table.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_CLM_SEGMENT]]
- ← [[CLM_CCM.ODS_HOUSEHOLD_DEMOGRAPHY]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| NBR_HH_MEMB_CHILDREN |
| AGE_MIN_HH_CHILD |
| AGE_MAX_HH_CHILD |
- ← [[CLM_CCM.ODS_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| CUSTOMER_AGE |
- ← [[CLM_CCM.HH_CHILD_PROBABILITY]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FLG_CUT_OFF |
| PRED_CHILD_AGE_SEGMENT |
| CUMUL_NBR_KV_PCT |
- ← [[ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |

## Target Tables (Outputs)
- → [[CLM_CCM.CCM_CUSTOMER_CLM_SEGMENT_N]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| CLM_LIVSFASE_SEGMENT_ADJ |
| CHILD_DERIVED_AGE_SEGMENT |
| CHILD_MODELLING_BASIS |
| PRED_FLG_CUT_OFF |
| PRED_CUMULATIVE_PCT |
- → [[CLM_CCM.CCM_CUSTOMER_CLM_SEGMENT]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| CLM_LIVSFASE_SEGMENT_ADJ |
| CHILD_DERIVED_AGE_SEGMENT |
| CHILD_MODELLING_BASIS |
| PRED_FLG_CUT_OFF |
| PRED_CUMULATIVE_PCT |
- → [[CLM_CCM.CCM_CUSTOMER_CLM_SEGMENT_O]]
- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_TIME |
| STATUS |
| STATUS_MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |

