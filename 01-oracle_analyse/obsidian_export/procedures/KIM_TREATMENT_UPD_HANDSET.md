# KIM_TREATMENT_UPD_HANDSET

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Updates the 'handset_key' column in the 'kim_treatment_dim' table. It assigns specific 'handset_key' values based on patterns found in the 'treatment_CD' column for records where 'handset_key' is less than 1, effectively categorizing or correcting handset information for various treatment types.

## Data Sources (Inputs)
- ← [[kim_treatment_dim]]
| Column Name |
|---|
| handset_key |
| treatment_CD |

## Target Tables (Outputs)
- → [[kim_treatment_dim]]
| Column Name |
|---|
| handset_key |

