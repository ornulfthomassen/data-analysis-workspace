# VYA_FTV_CVIEW_SAVE

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates data related to 'saved' customer churn cases from the last two years, joining information about the case itself, the associated customer account, and address details. It calculates various flags based on the presence of account, customer, and address IDs, and the relationship between geographic and residence FAR IDs.

## Data Sources (Inputs)
- ← [[CVIEW_STAGING."CASE"]]
| Column Name |
|---|
| CASENUMBER |
| CASE_SOLUTION__C |
| CLOSEDDATE |
| CREATEDDATE |
| DESCRIPTION |
| HOVEDGRUPPE_MANUELL__C |
| ORIGIN |
| UNDERGRUPPE_1_MANUELL__C |
| UNDERGRUPPE_2_MANUELL__C |
| SAVE_CANCELLATION_PERIOD__C |
| SAVE_CHANNEL__C |
| SAVE_COMPETITOR__C |
| SAVE_PRODUCT__C |
| SAVE_REASON_FOR_SAVED__C |
| SAVE_REASON_FOR_TERMINATION__C |
| SAVE_SAVED__C |
| A_NUMBER__C |
| CHANNEL_SUBCATEGORY__C |
| TERMINATION_SUBCATEGORY__C |
| TERMINATION_SUBCATEGORY_TV__C |
| TERMINATION_FROM_CHANNEL__C |
| ACCOUNTID |
| Related_Address__c |
| ISDELETED |
- ← [[CVIEW_STAGING.ACCOUNT]]
| Column Name |
|---|
| CUSTOMER_GROUP__C |
| KURTID__C |
| ID |
- ← [[CVIEW_STAGING.ADDRESS__C]]
| Column Name |
|---|
| ADRESSE_ID__C |
| FAR_ID__C |
| RESIDENCE_FAR_ID__C |
| ID |

