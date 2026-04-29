# GCP_COUNTERPART_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view extracts counterpart dimension data for loading into Google Cloud Platform (GCP), specifically for the CCDW.COUNTERPART target. It serves as a direct pass-through of specific columns from the source dimension table.

## Data Sources (Inputs)
- ← [[GALAXY.COUNTERPART_DIM]]
| Column Name |
|---|
| COUNTERPART_KEY |
| CP_CODE |
| CP_CLASSIFICATION_ID |
| CP_CLASSIFICATION_DESC |
| CP_INTERNAL_FLAG |
| START_DT_KEY |
| END_DT_KEY |
| STATUS |

