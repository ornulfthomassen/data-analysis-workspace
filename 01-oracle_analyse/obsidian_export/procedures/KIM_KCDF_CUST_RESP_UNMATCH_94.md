# KIM_KCDF_CUST_RESP_UNMATCH_94

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Iteratively updates specific customer response records within the KIM_customer_response table, setting 'CONTACT_KEY' to -1 and 'used_flg' to 0 for all records originating from 'SOURCE_SYSTEM_KEY' 94. It commits changes periodically to manage transaction size.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_customer_response]]
| Column Name |
|---|
| CUST_RESPONSE_KEY |
| SOURCE_SYSTEM_KEY |

## Target Tables (Outputs)
- → [[KIM_customer_response]]
| Column Name |
|---|
| CONTACT_KEY |
| used_flg |

