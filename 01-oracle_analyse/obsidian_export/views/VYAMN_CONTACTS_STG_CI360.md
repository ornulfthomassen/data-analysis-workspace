# VYAMN_CONTACTS_STG_CI360

**Schema:** `CCM` | **Type:** `View`

## Description
Extracts and transforms contact event data from SAS360_COMMON, enriching it with metadata, customer, subscription, and product information from various CRM and CLM analytical schemas, for staging. This view serves to prepare detailed contact event records, including associated campaign, customer, and product attributes, for further analysis or loading into a data warehouse (referred to as Mjøsa in comments).

## Data Sources (Inputs)
- ← [[SAS360_COMMON.SAS360_CONTACTS]]
| Column Name |
|---|
| CONTACT_ID |
| CONTACT_DTTM |
| CHANNEL |
| TASK_CD |
| TASK_NM |
| TASK_VERSION_ID |
| SEGMENT_VERSION_ID |
| SUBJECT_KEY |
| RESPONSE_TRACKING_CD |
| BUSINESS_UNIT |
- ← [[SAS360_COMMON.SAS360_CONTACTS_METADATA_KIM]]
| Column Name |
|---|
| TASK_VERSION_ID |
| SEGMENT_VERSION_ID |
| CLMPROGRAM |
| ACTIVITYID |
| ACTIVITYDESC |
| ACTIVITYMAINOBJ |
| CAMPAIGNID |
| ACTIVITYOBJ |
| ACTIVITYTP |
| SEGMENT_MAP_CD |
| CAMPAIGNDESC |
| CHANNEL |
| CLMPLAN |
| SEGMENT_CD |
| PREVACTIVITYID |
| PRODACT1 |
| PRODACT2 |
| PRODID1 |
| PRODID2 |
| PRODTP1 |
| PRODTP2 |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_KEY |
| CUSTOMER_SK |
- ← [[SAS360_COMMON.SAS360_SUPPL_SUBJECTS]]
| Column Name |
|---|
| SUBJECT_KEY |
| RESPONSE_TRACKING_CD |
| SUBJECT_TYPE |
| SUPPL_SUBJECT_KEY |
| CURRENT_PRODUCT_ID |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
- ← [[CLM_CCM.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_POID |
| PRODUCT_SOURCE_SYSTEM_ID |
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_AREA |
| PRODUCT_TECHNOLOGY |
| PRODUCT_CATEGORY |
| PRODUCT_GROUP |
| PRODUCT_REPORTING |
| PRODUCT_PAYMENT |
| PRODUCT_FAMILY_NAME |

