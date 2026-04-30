# V_SUBSCR_FB_MEMBERS

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive view of subscription data, particularly for fixed broadband members, by enriching raw subscription records with product details (name, family) and date information from dimension tables. This view likely serves analytical or reporting purposes for CRM, offering insights into subscriptions, offers, agreements, and associated product characteristics over time.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCR_FB_MEMBERS_2018_MV_SRG]]
| Column Name |
|---|
| DATE_ID |
| SUBSCRIPTION_ID |
| SOURCE_SUBSCRIPTION_ID |
| SUBSCRIBED_OFFER_ID |
| SUBSCRIBED_COMPONENT_ID |
| SD_PRODUCT_OFFER_ID |
| SOURCE_SD_PRODUCT_OFFER_ID |
| OFFER_VFD |
| OFFER_VTD |
| OFFER_CONFIG_VFD |
| OFFER_CONFIG_VTD |
| FB_AGREEMENT_ID |
| SB_AGREEMENT_ID |
| SD_AGREEMENT_ID |
| SOURCE_SD_AGREEMENT_ID |
| SD_AGREE_VFD |
| SD_AGREE_VTD |
| FB_DATABONUS_SIZE_GB |
| FB_NUM_PRODUCTS |
| NO_MOBILE |
| NO_BEDRIFT |
| NO_MBB |
| NO_SWAP |
| FIXED_TELEPHONY |
| FIXED_BROADBAND |
| DATABONUS_ACCESS_PRODUCT_LIST |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |

- ← [[GALAXY.DATE_DIM_MV]]
| Column Name |
|---|
| DATE_KEY |
| DAY |


