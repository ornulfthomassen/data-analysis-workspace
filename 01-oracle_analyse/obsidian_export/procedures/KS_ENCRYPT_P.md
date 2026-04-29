# KS_ENCRYPT_P

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure truncates the `CRM_ANALYSE.KS_ENCRYPT_NUM` table and then inserts encrypted employee identifiers along with a sequential number. The employee identifiers are derived from distinct non-null `EMPLOYEE_ID` or `EMPLOYEE_NUMBER` columns found in `crm_analyse.ks_interaction` and `CRM_ANALYSE.KS_ORDER_LINE_REP` tables. The `EMPL_NUM` column is populated using the `ENCRYPT_SEQ` sequence.

## Data Sources (Inputs)
- ← [[crm_analyse.ks_interaction]]
| Column Name |
|---|
| EMPLOYEE_ID |
| EMPLOYEE_NUMBER |
- ← [[CRM_ANALYSE.KS_ORDER_LINE_REP]]
| Column Name |
|---|
| EMPLOYEE_ID_ORD |
| EMPLOYEE_NUMBER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KS_ENCRYPT_NUM]]
| Column Name |
|---|
| EMPLOYEE_NUMBER |
| EMPL_NUM |

