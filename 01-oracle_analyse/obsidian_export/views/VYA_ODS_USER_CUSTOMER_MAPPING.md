# VYA_ODS_USER_CUSTOMER_MAPPING

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a unified mapping between user IDs and customer information. It joins the CONNECT_ID_LINK table with the CUSTOMER_ODS table based on CUSTOMER_ID, filtering for active and primary connections (RANK_CONNECTION = 1 and ACTIVE_FLAG = 'Y'). It provides user ID, customer surrogate key, registration/change datetimes, and a casted customer link quality.

## Data Sources (Inputs)
- ← [[ODS.CONNECT_ID_LINK]]
| Column Name |
|---|
| USER_ID |
| INFO_REG_DATE |
| INFO_CHG_DATE |
| CUST_LINK_QUALITY |
| CUSTOMER_ID |
| RANK_CONNECTION |
| ACTIVE_FLAG |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_SK |
| CUSTOMER_ID |

