# VYA_CUSTOMER_ACTIVITY_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a harmonized and anonymized view of customer activity logs by integrating data from various customer-related tables. It constructs detailed event descriptions based on hierarchical event levels and anonymizes sensitive information (like numbers, T-signs, emails, and URLs) within these descriptions using regular expressions, intended for analytical purposes (e.g., Mjøsa/Viya).

## Data Sources (Inputs)
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
| Column Name |
|---|
| ACT_CUST_ID |
| INFO_REG_DATE |
| ACT_EVENT_LEVEL1_ID |
| ACT_EVENT_LEVEL2_ID |
| ACT_EVENT_LEVEL3_ID |
| ACT_EVENT_LEVEL4_ID |
| ACT_LOG_ID |
| DESCRIPTION_ID |
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER_LINK]]
| Column Name |
|---|
| ACT_CUST_ID |
| INFO_REG_DATE |
| INTERNAL_CUST_ID |
| INFO_IS_DELETED |
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER]]
| Column Name |
|---|
| INTERNAL_CUST_ID |
| INFO_REG_DATE |
| KURT_ID |
| CUST_ID |
| INFO_IS_DELETED |
- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| KURT_ID |
| INFO_IS_DELETED |
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
| Column Name |
|---|
| DESCRIPTION_ID |
| DESCRIPTION_1 |
- ← [[CUSTOMERLOG.ACTIVITY_EVENT]]
| Column Name |
|---|
| ACT_EVENT_ID |
| ACT_EVENT_NAME |
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_SK |

