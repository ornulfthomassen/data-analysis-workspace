# GCP_ADM_CUSTOMER_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
The view `CCM.GCP_ADM_CUSTOMER_CURRENT` provides a consolidated, current-month snapshot of customer and household data. It integrates demographic information, communication preferences, life stage segmentation, household composition, detailed subscription counts for various product types (mobile, broadband, fiber), financial metrics like total net revenue (both owner and user), and network coverage details. This view is intended for loading comprehensive customer data into analytical systems.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_CHAR |
| PERIOD_MONTH_DATE |
| FIRST_DATE |
- ← [[CCM.VYA_ADM_CURRENT_USAGE_MONTH]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PREV1_PERIOD_MONTH_CHAR |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| CUSTOMER_AGE |
| CUSTOMER_ID |
| CUSTOMER_SK |
| DATE_OF_BIRTH |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
- ← [[CCDW.CUSTOMER]]
| Column Name |
|---|
| GENDER |
| KURT_ID |
- ← [[ODS.CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| TM_IND_BR |
| DM_IND_BR |
| TM_IND_INTERNAL |
| DM_IND_INTERNAL |
| EMAIL_IND |
| SMS_IND |
| EMAIL_ADDRESS |
| SMS_NUMBER |
| CUSTOMER_ID |
- ← [[CLM_CCM.CCM_CUST_CONTACT_ADDRESS_V]]
| Column Name |
|---|
| KURT_ID |
| POSTCODE_ID |
| POSTCODE_NAME |
- ← [[CLM_ADM.ADM_SUBS_USAGE_MOB_MONTH_AGG]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MB_DATA |
| PERIOD_MONTH_KEY |
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
| Column Name |
|---|
| KURT_ID |
| CU_NO_MPP |
| CU_NO_MPR |
| CU_NO_MBB |
| CU_NO_FBR |
| CU_NO_MPP_USR |
| CU_NO_MPR_USR |
| CU_NO_MBB_USR |
| CU_NO_FBR_USR |
| CU_NO_MPP_BUS_USR |
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO_V]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| HOUSEHOLD_MEMBER_COUNT |
| BOLIGTYPE |
| FAR_ID |
| HH_NO_MPP_USR |
| HH_NO_MPP_BUS_USR |
| HH_NO_MPR_USR |
| HH_NO_MBB_USR |
| HH_NO_MBB_BUS_USR |
| HH_NO_FIX_BBT_FTV_HH_ADR |
| HH_NO_FIX_BBT_TNN_HH_ADR |
| HH_NO_FIX_POTS_BUS_HH_ADR |
| HH_NO_FIX_POTS_HH_ADR |
| HH_NO_FBB_FBR_FTV_HH_ADR |
| HH_NO_FBB_FBR_FTV_OTHER_ADR |
| HH_NO_FBB_FBR_FTV_UNKNOWN_ADR |
| HH_NO_FBB_FBR_TNN_HH_ADR |
| HH_NO_FBB_FBR_TNN_OTHER_ADR |
- ← [[CLM_CCM.CCM_FAR_V]]
| Column Name |
|---|
| FARID |
| STREETPOSTALCODE |
| MUNICIPALITY_CODE |
| BASIC_STATISTICAL_UNIT_ID |
- ← [[CLM_CCM.CCM_COVERAGE_NEW_V]]
| Column Name |
|---|
| FARID |
| MB_QUALITY_4G_PLUS |
| MB_QUALITY_4G |
| MB_BEST_MOB_COVERAGE |
| MB_BEST_MOB_QUALITY |
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
| Column Name |
|---|
| CUSTOMER_SK_OWNER |
| PERIOD_MONTH_KEY |
| NET_FEE |
| NET_USE |
| NO_MPP |
| MPP_NO_DAYS_ACTIVE |
| MPP_NO_DAYS_PROD |
| NO_MPR |
| MPR_NO_DAYS_ACTIVE |
| MPR_NO_DAYS_PROD |
| NO_MBB |
| MBB_NO_DAYS_ACTIVE |
| MBB_NO_DAYS_PROD |
| NO_FIX |
| FIX_NO_DAYS_ACTIVE |
| FIX_NO_DAYS_PROD |
- ← [[CLM_ADM.ADM_CUSTOMER_USER_SUBS_AGG]]
| Column Name |
|---|
| CUSTOMER_SK_USER |
| PERIOD_MONTH_KEY |
| NET_FEE |
| NET_USE |
- ← [[CLM_ADM.ADM_MOB_CUST_U_TALE_P_REV_3MO]]
| Column Name |
|---|
| CUSTOMER_SK_USER |
| PERIOD_MONTH_KEY |
| MAIN_SUBSCRIPTION_REV |
| NET_REVENUE_ADJUSTED |
| MAIN_SUBSCRIPTION_TYPE |

