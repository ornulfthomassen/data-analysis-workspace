# VYA_CDC_EMAIL_ADDRESS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a transformed representation of email address data from the CDC.EMAIL_ADDRESS table. It includes email address validation and obfuscation logic: if an email is malformed (missing '@' or having multiple '@' symbols), it's flagged; otherwise, it applies a specific obfuscation pattern to the email address while also exposing associated registration and change information.

## Data Sources (Inputs)
- ← [[CDC.EMAIL_ADDRESS]]
| Column Name |
|---|
| ADDRESS_TYPE_LINK_ID |
| EMAIL_ADDRESS |
| INFO_REG_USER_NAME |
| INFO_REG_APPL_NAME |
| INFO_REG_DATE |
| INFO_CHG_USER_NAME |
| INFO_CHG_APPL_NAME |
| INFO_CHG_DATE |
| INFO_IS_DELETED |

