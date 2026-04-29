# KIM_CONTACT_KS

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure enriches records in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table by adding 'TALK_SECONDS', 'CONTACT_LOCATION', and 'CONTACT_TEAM' information. It processes records in two batches based on the length of the `CONN_ID`. For `CONN_ID`s with length 16, it joins with `KS_READER.KS_TRAFFIC` and `KS_READER.KS_TRAFFIC_CALLS` to derive the information. For `CONN_ID`s with length less than 16, it directly uses `CONN_ID` to join with `GALAXY.SALESTIPS_KS_DIM_V`. Updates are committed periodically in batches of 100,000 records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_DTTM |
| CHANNEL_KEY |
| SOURCE_SYSTEM_KEY |
| CONN_ID |
| MEASURE_TYPE |
| CONTACT_TEAM |
| CONTACT_KEY |
| CONTACT_LOCATION |
- ← [[KS_READER.KS_TRAFFIC]]
| Column Name |
|---|
| CONN_ID |
| TRUNC_DATE |
| TALK_SECONDS |
| AGENT_ID |
| PK |
- ← [[KS_READER.KS_TRAFFIC_CALLS]]
| Column Name |
|---|
| PK |
| TRUNC_DATE |
| LAST_AGENT_ID |
- ← [[GALAXY.SALESTIPS_KS_DIM_V]]
| Column Name |
|---|
| AGENT_ID |
| HIST_FROM_DATE |
| HIST_TO_DATE |
| SITE_NAME |
| TEAM_NAME |
| EMPLOYEE_NUMBER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_SECONDS |
| CONTACT_LOCATION |
| CONTACT_TEAM |
| CONTACT_KEY |

