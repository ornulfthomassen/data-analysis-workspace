# V_MPORT

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and enriches mobile number portability (MNP) order and event data with detailed subscription information, source system mappings, and profit segment categorization. It also calculates various date-related fields and applies a ranking to select the most relevant subscription record based on end and start dates.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]
| Column Name |
|---|
| PORT_DATE |
| ORDER_ID |
| STATUS |

- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
| Column Name |
|---|
| ORDER_ARRIVAL_DATE |
| ORDER_ID |
| ORDER_PHONE_NUM |
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
| SOURCE_SYSTEM_KEY |
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_ID |

- ← [[CRM_ANALYSE.PROFITSEGMENT_MOBILE]]
| Column Name |
|---|
| SEGMENT_ID |
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |

- ← [[PROFIT.CP_CAT_BED_PRIV]]
| Column Name |
|---|
| CATEGORY |
| SUBSCR_ID |
| PERIOD_ID |


