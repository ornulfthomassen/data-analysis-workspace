# V_MB_USAGE_CURRENT

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a comprehensive, current snapshot of mobile subscription data for CRM analysis, consolidating subscription details, product information, customer demographics (owner and user), device specifics, data usage patterns, and various segmentation and campaign-related attributes for mobile telephony services.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| MAIN_PRODUCT_ID |
| OWNER_KURT_ID |
| MAIN_NUMBER |
| DAYS_LEFT_OF_BINDINGPERIOD |
| TERMINAL_MODEL_NAME |
| NO_ROAMING_EU_SUM_12MO |
| MB_TOTAL_PREV1 |
| MB_TOTAL_PREV2 |
| MB_TOTAL_PREV3 |
| AVG_MB_TOTALT |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| USER_KURT_ID |
| SUBSCRIPTION_ID |
| TERMINAL_MODEL_ID |
| SUBSCRIPTION_TYPE |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PORTFOLIO |
| PRODUCT_BRAND |
| MONTHLY_PRICE |
| INCLUDED_DATA |
| INCLUDED_MINUTES |
| INCLUDED_MMS |
| INCLUDED_SMS |

- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| AGE |

- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_ID |

- ← [[CLM_CCM.CCM_SUBSCRIPTION_INFO_2]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| CONTRACT_TYPE |

- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| MODEL_ID |
| MARKETING_NAME_L1 |

- ← [[CCM.PER_TERMINAL_INFO]]
| Column Name |
|---|
| MODEL_ID |
| TOUCH_SCREEN |

- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| OFFER_CATEGORY |
| ACTION_CATEGORY |
| CURRENT_VERSION |
| TREATMENT_CD |
| CAMP_OFFER_PRIORITY |

- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT]]
| Column Name |
|---|
| KURT_ID |
| MODEL_ID |
| START_DATE |
| END_DATE |
| SEGMENT_ID |


