# ADM_KURT_CONNECTID_HARDLINK_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
Aggregates user account, email, and phone data, extracting 'KURT_ID' and 'TNUID' from account identifiers based on 'HARDLINK_' and 'TNUID_TSS-' patterns, respectively. For each user, it retrieves the most recent verified phone information (MSISDN and verification time) and their email address. The view filters for user accounts containing 'HARDLINK_' in their ID, specific Norwegian MSISDN ranges, and explicitly verified phone numbers.

## Data Sources (Inputs)
- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_USER_ID |
| ACC_MSISDN |
- ← [[COMOYO.FIM_USER_EMAILS]]
| Column Name |
|---|
| USER_ID |
| EMAIL_ADDRESS |
- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| USER_ID |
| PH_MSISDN |
| PH_VERIFIED |
| PH_VERIFICATION_TIME |

