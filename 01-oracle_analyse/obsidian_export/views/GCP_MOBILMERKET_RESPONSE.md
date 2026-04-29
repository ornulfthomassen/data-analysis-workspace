# GCP_MOBILMERKET_RESPONSE

**Schema:** `CCM` | **Type:** `View`

## Description
Prepares aggregated Mobilmerket response and participant data from third-party services for reporting in GCP BigQuery via Denodo, including hashing of IP addresses.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_ANSWER]]
| Column Name |
|---|
| PARTICIPANT_ID |
| QUESTION |
| BUTTON |
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_PARTICIPANT]]
| Column Name |
|---|
| PARTICIPANT_ID |
| OID |
| IP |
| START_DATE |
| END_DATE |
| VERSION |

