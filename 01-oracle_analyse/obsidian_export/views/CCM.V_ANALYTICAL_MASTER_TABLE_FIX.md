# V_ANALYTICAL_MASTER_TABLE_FIX

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `V_ANALYTICAL_MASTER_TABLE_FIX`, constructs a comprehensive analytical master dataset primarily for fixed-line telecommunication subscriptions. It integrates monthly period dimensions, detailed subscription history, customer demographic information, and aggregated usage and revenue data. The view calculates and presents various key performance indicators (KPIs) and metrics, including voice call activity (domestic and international) over the preceding three months, different revenue components (such as periodic fees, discounts, and usage-based charges), and subscription attributes like brand, type, product details, and active days. It applies stringent filters to include only specific customer types ('PU', 'P', 'PC') and statuses ('K'), and subscription types ('Telefoni - POTS', 'Telefoni - BBT'), while also explicitly excluding a list of known test customer IDs. The resulting dataset is ordered by month and subscription ID, indicating its use for time-series analysis of fixed-line services.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| PERIOD_MONTH_KEY_CHAR |
| LAST_DATE |

- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| CUSTOMER_SK_OWNER |
| CUSTOMER_SK_USER |
| PRODUCT_BRAND |
| SUBS_NO_DAYS_ACTIVE |
| PROD_NO_DAYS_ACTIVE |
| NO_DAYS_LAST_START |
| NO_DAYS_LAST_CHANGE |
| NO_DAYS_BIND_START |
| NO_DAYS_BIND_END |
| PRODUCT_OFFER_ID |
| PRODUCT_NAME |

- ← [[CLM_ADM.ADM_CUSTOMER_INFO_HIST]]
| Column Name |
|---|
| CUSTOMER_SK |
| PERIOD_MONTH_KEY |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |

- ← [[CLM_ADM.ADM_SUBSCR_DETAIL_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| SUBS_TYPE |
| SOURCE_SYSTEM_KEY |
| PRODUCT_ID |
| FRIFAM_NO_DAYS_ACTIVE |

- ← [[CLM_ADM.ADM_SUBSCRIPTION_AGG]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| NUMBER_SPEECH_NORGE_PREV1 |
| NUMBER_SPEECH_NORGE_PREV2 |
| NUMBER_SPEECH_NORGE_PREV3 |
| NUMBER_SPEECH_UTLAND_PREV1 |
| NUMBER_SPEECH_UTLAND_PREV2 |
| NUMBER_SPEECH_UTLAND_PREV3 |
| DURAT_SPEECH_NORGE_PREV1 |
| DURAT_SPEECH_NORGE_PREV2 |
| DURAT_SPEECH_NORGE_PREV3 |
| DURAT_SPEECH_UTLAND_PREV1 |
| DURAT_SPEECH_UTLAND_PREV2 |
| DURAT_SPEECH_UTLAND_PREV3 |
| KR_SPEECH_NORGE_PREV1 |
| KR_SPEECH_NORGE_PREV2 |
| KR_SPEECH_NORGE_PREV3 |
| KR_SPEECH_UTLAND_PREV1 |
| KR_SPEECH_UTLAND_PREV2 |
| KR_SPEECH_UTLAND_PREV3 |
| GROSS_PERIODIC_FEE_FULL |
| NET_FEE |
| NET_USE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_PERIODIC_FEE |
| NET_INITIATION_FEE |
| NET_TERMINATION_FEE |
| NET_DISCOUNT_FIXED_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| NET_AMOUNT_USE |
| NET_DISCOUNT_AMOUNT_USE |


