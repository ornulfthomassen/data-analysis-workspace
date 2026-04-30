# VIYA_KIM_SJEKK

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of campaign performance, customer interactions, and related product information, including calculated KPIs such as presented volume and initial sales volume.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| VOLUME |
| CONTACT_DTTM |
| CONTACT_MONTH_KEY |
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| KURT_ID_OWNER |
| KURT_ID_USER |
| ORDER_MATCH_KEY |
| ORDER_RANK |
| ORDER_RANK_GROUP_KEY |
| CONTACT_KEY |
| ORDER_ID |
| ORDER_DT_KEY |
| RESPONSE_KEY |
| CHANNEL_KEY |

- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
| Column Name |
|---|
| ACTIVITY_ID |
| PROGRAM |
| CAMPAIGN |
| PRODUCT_KEY_1 |
| PRODUCT_KEY_2 |
| PRODUCT_ACT1 |
| PRODUCT_ACT2 |
| INTERACTION_CD |
| CONTACT_KEY |

- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]
| Column Name |
|---|
| RESPONSE_NM |
| RESPONSE_GROUP |
| RESPONSE_KEY |

- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
| Column Name |
|---|
| CHANNEL_COMMON_NM |
| CHANNEL_KEY |

- ← [[CRM_ANALYSE.PRODUCT_DIM_V]]
| Column Name |
|---|
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |
| PRODUCT_KEY |


