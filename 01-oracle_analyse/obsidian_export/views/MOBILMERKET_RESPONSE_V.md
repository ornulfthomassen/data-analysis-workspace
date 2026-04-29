# MOBILMERKET_RESPONSE_V

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates response and participant information from the 'Mobilmerket' system by joining answer data with participant data based on participant ID.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_ANSWER]]
| Column Name |
|---|
| PARTICIPANT_ID |
| QUESTION |
| BUTTON |
| OID |
| IP |
| START_DATE |
| END_DATE |
| VERSION |
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_PARTICIPANT]]
| Column Name |
|---|
| participant_id |

