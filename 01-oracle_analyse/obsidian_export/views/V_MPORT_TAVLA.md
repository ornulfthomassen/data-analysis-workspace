# V_MPORT_TAVLA

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates mobile number portability (MNP) and subscription details, filtering for recent porting orders ('TIL CONSUMER' status within the last 30 days). It selects the latest subscription record for each main number based on end and original start dates, calculates various date-related fields (e.g., porting duration, profit month link keys), and provides a comprehensive overview of ported subscriptions for analytical purposes.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
| Column Name |
|---|
| ORDER_ID |
| STATUS |
| PORT_DATE |
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_PHONE_NUM |
| ORDER_ARRIVAL_DATE |
| SERVICE_PROVIDER_ID_OUT |
| SERVICE_PROVIDER_ID_OUT_NAME |
| ORDER_STATUS_ID |
| FETCHED_DATE |
- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| KURT_ID_OWNER |
| KURT_ID_USER |
| KURT_ID_PAYER |
| MAIN_NUMBER |
| MARKET_AREA_ID |
| ORIGINAL_START_DATE |
| PARENT_SUBSCRIPTION_ID |
| PRODUCT_OFFER_ID |
| START_DATE |
| END_DATE |
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |

