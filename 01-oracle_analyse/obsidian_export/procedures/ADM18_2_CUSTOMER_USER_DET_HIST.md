# ADM18_2_CUSTOMER_USER_DET_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle SQL procedure populates or updates the `CRM_ANALYSE.ADM_CUSTOMER_USER_DETAIL_HIST` table with aggregated customer user details and social network analysis (SNA) metrics. It processes data for a specified month or a range of months. If the target table does not exist, it creates it along with its primary index and partitions. For each month within the processing range, it checks for existing data, creates a new partition if needed, and then inserts derived and aggregated data by joining several source tables related to subscriptions, product types, and SNA. It also logs the load history and gathers table statistics.

## Data Sources (Inputs)
- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DAY |
| YEAR_MONTH_NUMBER |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| KURT_ID_USER |
| MAIN_NUMBER |
- ← [[CRM_ANALYSE.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| MB_TOT_PREV1 |
| MB_TOT_PREV2 |
| MB_TOT_PREV3 |
| NET_FEE |
| NET_USE |
- ← [[CRM_ANALYSE.ADM_MAIN_NUMBER_BANKID]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| MAIN_NUMBER |
- ← [[CCDW_CONSUMERANALYSE.CON_SNA_AGG]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_KEY |
| SNA_CP |
| SNA_CP_W |
| SNA_CP_W_REL |
| SNA_DEGREE |
| SNA_DEGREE_W |
| SNA_FRIEND10_CP |
| SNA_FRIEND_OFF_REL |
| SNA_FRIEND_OFF_W |
| SNA_SMS_LATE_FRAC |
| SNA_VOICE_LATE_FRAC |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_CUSTOMER_USER_DETAIL_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID_USER |
| ANTALL_MOB |
| MAIN_SUBSCR_MB_LAST1 |
| MAIN_SUBSCR_MB_3MO |
| MAIN_SUBSCR_NET_FEE |
| MAIN_SUBSCR_NET_USE |
| MAIN_SUBSCRIPTIPON_ID_MB |
| MAIN_SUBSCRIPTIPON_ID_KR |
| NO_BANKID |
| MPP_SNA_CP |
| MPP_SNA_CP_W |
| MPP_SNA_CP_W_REL |
| MPP_SNA_DEGREE_SUM |
| MPP_SNA_DEGREE_MAX |
| MPP_SNA_DEGREE_W |
| MPP_SNA_FRIEND10_CP |
| MPP_SNA_FRIEND_OFF_REL |
| MPP_SNA_FRIEND_OFF_W |
| MPP_SNA_SMS_LATE_FRAC |
| MPP_SNA_VOICE_LATE_FRAC |
| MPR_SNA_CP |
| MPR_SNA_CP_W |
| MPR_SNA_CP_W_REL |
| MPR_SNA_DEGREE_SUM |
| MPR_SNA_DEGREE_MAX |
| MPR_SNA_DEGREE_W |
| MPR_SNA_FRIEND10_CP |
| MPR_SNA_FRIEND_OFF_REL |
| MPR_SNA_FRIEND_OFF_W |
| MPR_SNA_SMS_LATE_FRAC |
| MPR_SNA_VOICE_LATE_FRAC |
| MOB_SNA_CP |
| MOB_SNA_CP_W |
| MOB_SNA_CP_W_REL |
| MOB_SNA_DEGREE_SUM |
| MOB_SNA_DEGREE_MAX |
| MOB_SNA_DEGREE_W |
| MOB_SNA_FRIEND10_CP |
| MOB_SNA_FRIEND_OFF_REL |
| MOB_SNA_FRIEND_OFF_W |
| MOB_SNA_SMS_LATE_FRAC |
| MOB_SNA_VOICE_LATE_FRAC |

