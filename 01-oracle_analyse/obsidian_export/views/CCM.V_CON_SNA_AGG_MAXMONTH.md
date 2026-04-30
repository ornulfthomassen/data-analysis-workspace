# V_CON_SNA_AGG_MAXMONTH

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a snapshot of Social Network Analysis (SNA) aggregated data from the `CON_SNA_AGG` table, specifically filtering for records corresponding to the latest available month (maximum `PERIOD_MONTH_KEY`).

## Data Sources (Inputs)
- ← [[CCM.CON_SNA_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| MAIN_NUMBER |
| USER_CUSTOMER_KEY |
| SNA_DEGREE |
| SNA_DEGREE_W |
| SNA_SMS_IN_FRAC |
| SNA_VOICE_IN_FRAC |
| SNA_VOICE_LATE_FRAC |
| SNA_SMS_LATE_FRAC |
| SNA_CP_W |
| SNA_CP_W_REL |
| SNA_CP |
| SNA_CP_REL |
| SNA_FRIEND5_CP |
| SNA_FRIEND10_CP |
| SNA_FRIEND_OFF |
| SNA_FRIEND_OFF_REL |
| SNA_FRIEND_OFF_W |
| SNA_FRIEND5_OFF |
| SNA_SMS_OFF |
| SNA_VOICE_OFF |
| SNA_SMS_CP |
| SNA_VOICE_CP |
| SNA_SMS_IN_CP |
| SNA_VOICE_IN_CP |
| SNA_SMS_LATE_CP |
| SNA_VOICE_LATE_CP |
| RUN_ID |
| SEQ_ID |


