# VYA_ODS_CUSTOMER

**Schema:** `CCM` | **Type:** `View`

## Description
Creates a comprehensive customer profile view by integrating data from various operational and analytical sources (ODS, CRM, CCDW, Talkmore). It consolidates customer demographics, subscription details (mobile, fixed, FTV, owner/payer/user counts), usage statistics, communication preferences, and Talkmore product usage. The view also includes derived attributes like age, age group, and birth year/month, and provides a default 'unknown' customer record for cases where a customer_sk is -1.

## Data Sources (Inputs)
- ← [[TALKMORE.TALKMORE_MATCH]]
| Column Name |
|---|
| CUSTOMER_KEY |
| NO_TKM_MPP_USER |
| NO_TKM_MPR_USER |
| NO_TKM_MBB_USER |
| NO_TKM_MPP_BUS_USER |
| NO_TKM_OTHER_USER |
| NO_TKM_MPP_OWNER |
| NO_TKM_MPR_OWNER |
| NO_TKM_MBB_OWNER |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| HOUSEHOLD_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
| DATE_OF_BIRTH |
| DATE_OF_BIRTH_NUMBER |
| COMMERCIAL_CUSTOMER_NAME |
| ORGANISATION_NUMBER |
| AVG_MONTH_NET_AMOUNT |
| AVG_MONTH_GROSS_AMOUNT |
| OWNER_MOB_SUB_NUM |
| PAYER_MOB_SUB_NUM |
| USER_MOB_SUB_NUM |
| USER_MOB_SUB_NUM_BIZ |
| USER_MOB_SUB_NUM_CONS |
| OWNER_FIX_SUB_NUM |
| PAYER_FIX_SUB_NUM |
| USER_FIX_SUB_NUM |
| USER_FIX_SUB_NUM_BIZ |
| USER_FIX_SUB_NUM_CONS |
| OWNER_FTV_SUB_NUM |
| PAYER_FTV_SUB_NUM |
| USER_FTV_SUB_NUM |
| USER_FTV_SUB_NUM_BIZ |
| USER_FTV_SUB_NUM_CONS |
| OWNER_MOB_AGR_NUM |
| NET_FEE_LAST_MONTH |
| TRAFFIC_NET_AMOUNT_THIS_MONTH |
| TRAFFIC_NET_AMOUNT_LAST_MONTH |
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| KURT_ID |
| GENDER |
- ← [[ODS.CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| CUSTOMER_ID |
| DM_IND_BR |
| TM_IND_BR |
| DM_IND_INTERNAL |
| TM_IND_INTERNAL |
| BR_DM_MAX_RES_APP_DTTM |
| BR_TM_MAX_RES_APP_DTTM |
| DM_MAX_RES_APP_DTTM |
| TM_MAX_RES_APP_DTTM |
| EMAIL_IND |
| EMAIL_ADDRESS |
| EMAIL_RA_MAX_DTTM |
| SMS_IND |
| SMS_NUMBER |
| SMS_RA_MAX_DTTM |
- ← [[CCDW.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| COUNTERPART_CODE |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |
- ← [[CRM_ANALYSE.ADM_AGE_GROUP_DIM]]
| Column Name |
|---|
| AGE_GROUP_KEY |
| AGE_GROUP_NAME_8C |
- ← [[DUAL]]

