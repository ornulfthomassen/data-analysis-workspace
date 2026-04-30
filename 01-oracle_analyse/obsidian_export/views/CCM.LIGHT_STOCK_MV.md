# LIGHT_STOCK_MV

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'LIGHT_STOCK_MV', provides a comprehensive, unified perspective on customer subscriptions and associated product, usage, and demographic data. It integrates detailed information from various sources including subscription details, product specifications, customer demographics (owner and user), household information, geographical data, terminal details, and historical data like rollover, porting, and swap agreements. The view calculates numerous key performance indicators (KPIs) and grouped metrics related to product usage (data, minutes, SMS), revenue, binding periods, and customer segments, enhancing analytical capabilities for CRM, marketing, and stock analysis. It also encrypts sensitive identifiers like owner ID, user ID, and main number.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| MAIN_PRODUCT_ID |
| OWNER_KURT_ID |
| USER_KURT_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_TYPE |
| MB_TOTAL_PREV1 |
| MB_TOTAL_PREV2 |
| MB_TOTAL_PREV3 |
| AVG_MB_TOTALT |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| PCT_USED_INCL_MB_SUBS_AVG_3MO |
| TREATMENT_CD |
| CAMP_OFFER_PRIORITY |
| SUBSCRIPTION_ID |
| DEVICE_TAC |
| PREVIOUS_PRODUCT_ID |
| ORIGINAL_START_DATE |
| MAIN_PRODUCT_START_DATE |
| END_DATE |
| ACTIVE_DAYS |
| DAYS_IN_PERIOD |
| START_DATE |
| NUMBER_SMS_DOMESTIC_PREV1 |
| NUMBER_SMS_DOMESTIC_PREV2 |
| NUMBER_SMS_DOMESTIC_PREV3 |
| MINUTES_SPEECH_DOMESTIC_PREV1 |
| MINUTES_SPEECH_DOMESTIC_PREV2 |
| MINUTES_SPEECH_DOMESTIC_PREV3 |
| MB_TOTAL_PREV_30_DAYS |
| PAYMENT_METHOD_ID |
| NO_MMS_DOM_AVG_3MO |
| PARENT_SUBSCRIPTION_ID |
| TERMINAL_MODEL_ID |
| PCT_P_USE_LAST1_BY_CUR_F_UNIT |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PORTFOLIO |
| DRM_COMMON_BRAND |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_REPORTING |
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
| GENDER |
| SMS_IND |
| EMAIL_IND |
| HOUSEHOLD_ID |
| CUSTOMER_STATUS_CD |

- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
| Column Name |
|---|
| KURT_ID |
| MAP_SEGMENT_ID |
| CLM_LIVSFASE_SEGMENT_ID |
| CU_NO_UNITS_QUALIFIED_FB |
| CU_AGRMT_FB_STATUS |
| CU_NO_FBB_COAX |
| CU_NO_FBB_FBR_FTV |
| CU_NO_MPP |
| CU_NO_MPP_USR |
| CU_NO_MPR |

- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_ID |
| END_DATE |

- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |

- ← [[GALAXY.SUBSCRIPTION_DIM]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| HANDSET_KEY_LAST_USED |

- ← [[CLM_CCM.CCM_SUBS_EQUIPMENT_INFO]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SIM_NETTWORK_SUPPORTED |
| SIM_FORM_FACTOR_NAME |
| SIM_ESIM_TYPE_NAME |
| LTE |
| UMTS |
| HSDPA |
| GPRS |
| EDGE |

- ← [[CLM_CCM.CCM_ROLLOVER]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| MB_ROLLOVER_GR_LAST_1 |
| MB_ROLLOVER_GR_LAST_2 |
| MB_ROLLOVER_GR_LAST_3 |
| MB_ROLLOVER_GR_LAST_1_DESC |
| MB_ROLLOVER_GR_LAST_2_DESC |
| MB_ROLLOVER_GR_LAST_3_DESC |
| MB_ROLLOVER_GR_NUM_LAST_1 |
| MB_ROLLOVER_GR_NUM_LAST_2 |
| MB_ROLLOVER_GR_NUM_LAST_3 |
| MB_ROLLOVER_LAST_1 |
| MB_ROLLOVER_LAST_2 |
| MB_ROLLOVER_LAST_3 |

- ← [[CRM_ANALYSE.HOUSEHOLD_LAT_LONG_SHOP_V]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| POSTNR |
| POSTSTED |
| KOMMUNENR |
| LATITUDE |
| LONGITUDE |

- ← [[CRM_ANALYSE.MUNICIPAL_DIM]]
| Column Name |
|---|
| MUNICIPAL_ID |
| COUNTY_ID |
| COUNTY |
| MUNICIPAL |

- ← [[CLM_CCM.CCM_TERMINAL_DETAIL]]
| Column Name |
|---|
| MODELID |
| PRODUCERNAME |
| MODELNAME |
| DEVICE_TOUCH_SCREEN |

- ← [[CLM_ADM.ADM_GSMA_MARKETING_NAME_DIM]]
| Column Name |
|---|
| TAC |
| MARKETING_NAME_L1 |

- ← [[CRM_ANALYSE.ADM_QUAL_OFFER_HIST_SUBSCR]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| OFFER_CATEGORY |
| ACTION_CATEGORY |
| CURRENT_VERSION |

- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| ORDER_SUBSCR_KEY |
| AGREED_DELIVERY_DT_KEY |
| SERVICE_PROVIDER_TO_KEY |
| KPI_PORTING_OUTBOUND |
| ORDER_LINE_TYPE_KEY |
| ORDERLINE_PRODUCT_KEY |
| MARKET_AREA_KEY |
| ORDER_STATUS_KEY |

- ← [[GALAXY.MARKET_AREA_DIM]]
| Column Name |
|---|
| MARKET_AREA_KEY |

- ← [[CLM_CCM.CCM_AGREEMENT]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_NAME |
| KURT_ID_OWNER |

- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER]]
| Column Name |
|---|
| AGREEMENT_KEY |
| PRODUCT_KEY |
| MEMB_VALID_TO_DATE |
| SUBSCRIPTION_KEY_USE |

- ← [[ADHOC_BS.MK_1727_RES]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| MB_M1 |
| MB_M2 |
| MB_M3 |
| MB_3MND_ADJ |
| CORE_REVENUE_M1 |
| CORE_REVENUE_M2 |
| CORE_REVENUE_M3 |
| CORE_REVENUE_3MND_ADJ |
| NKR_BINDING_M1 |
| NKR_BINDING_M2 |
| NKR_BINDING_M3 |
| NKR_BINDING_3MND_ADJ |


