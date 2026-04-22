# V_MB_USAGE_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive current analytical snapshot of mobile telephony subscriptions (both PrePaid and PostPaid). It integrates detailed information about subscriptions (product details, pricing, included services, contract terms), associated customer demographics (owner and user age, segmentation), terminal device information, and crucially, recent mobile data usage patterns and utilization percentages. It also includes marketing-related flags like 'treatment code' and 'retention flag', suggesting its use for customer analytics, retention strategies, and understanding subscriber behavior related to mobile data consumption.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
- ← [[CLM_CCM.CCM_SUBSCRIPTION_INFO_2]]
- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[PER_TERMINAL_INFO]]
- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]

