# LIGHT_AGREEMENT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, LIGHT_AGREEMENT_V, provides a comprehensive, denormalized view of customer agreement data. It combines information from customer agreements, agreement members, customer demographics, household details, subscription information, product definitions, dealer details, and handset information. The view enriches the data with calculated metrics such as week numbers for agreement validity, product family categorization based on product attributes, mobile data usage groups, and various 'SikkerID' and 'SAFE' product flags, aiming to provide a unified dataset for CRM analysis.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_AGREEMENT]]
| Column Name |
|---|
| AGREEMENT_KEY |
| AGREEMENT_OFFER_NAME |
| KURT_ID_owner |
| LOAD_DATE |
| RUN_DATE |
| SOURCE_AGREEMENT_ID |
| VALID_FROM_DATE |
| VALID_TO_DATE |

- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER]]
| Column Name |
|---|
| AGREEMENT_KEY |
| SUBSCRIPTION_KEY_AGR |
| PRODUCT_DESC |
| PRIM_PRODUCT_DESC |
| PRODUCT_KEY |
| LOAD_DATE |
| MEMB_VALID_TO_DATE |
| MEMB_VALID_FROM_DATE |
| MAIN_NUMBER_USE |
| MAIN_NUMBER_AGR |
| KURT_ID_MEMBER |
| IMEI |
| EUREKA_IMEI |

- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
| Column Name |
|---|
| AGREEMENT_KEY |
| order_line_type_key |
| orderline_product_key |
| order_line_id |
| DEALER_KEY |

- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| DRM_SALES_CHANNEL_GEN03_DESC |
| DRM_SALES_CHANNEL_GEN04_DESC |
| DRM_SALES_CHANNEL_GEN05_DESC |
| DRM_SALES_CHANNEL_GEN07_DESC |
| DEALER_CHAIN_NAME |
| DEALER_NAME |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_NAME |
| SOURCE_PRODUCT_ID_1 |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_PRODUCT_CATEGORY |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PAYMENT |
| DRM_COMMON_REPORTING |
| DRM_COMMON_MARKET_PRODUCT |

- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| AGE |

- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| ANT_BEDRIFTER |
| FIXED_INTERNETT_DIALUP |
| FIXED_INTERNETT_DSL |
| FIXED_INTERNETT_DSL_UTENF_HS |
| FIXED_INTERNETT_FIBER |
| FIXED_INTERNETT_FIBER_UTENF_HS |
| FIXED_INTERNETT_WIMAX |
| FIXED_INTERNETT_WIMAX_UTENF_HS |
| FIXED_TALE |
| FIXED_TALE_HOS_ANDRE |
| FIXED_TALE_UTENF_HS |
| GRUNNKRETS |
| GRUNNKRETS_NR |
| HH_NO_DSL_ISP_LINES |
| HOUSEHOLD_TYPE |
| KOMMUNENR |
| MOBIL_INTERNETT |
| MOBIL_TALE |
| MOBIL_TALE_HOS_ANDRE |
| MULIG_ADSL_HOS_ANDRE |
| NO_MPR_USR |
| NO_U21_USR |
| POSTNR |
| POSTSTED |

- ← [[CLM_CCM.CCM_AGREEMENT_MEMBER_PIVOT_V]]
| Column Name |
|---|
| AGREEMENT_KEY |

- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
| Column Name |
|---|
| KURT_ID |
| MAP_SEGMENT_NAME |
| CLM_LIVSFASE_SEGMENT_NAME |
| CU_NO_MPR |
| CU_NO_MPP |
| CU_AGRMT_SFTY_EMAIL_MONITORING |
| CU_AGRMT_SFTY_STATUS |

- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| main_number |
| SUBSCRIPTION_TYPE |
| MB_TOTAL_PREV1 |
| MB_TOTAL_PREV2 |
| MB_TOTAL_PREV3 |
| AVG_MB_TOTALT |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| PCT_USED_INCL_MB_SUBS_AVG_3MO |
| NO_FB_GRUNNLAG |
| NO_FB_USERS |
| NO_SWAP |
| NO_Postpaid |
| NO_DSL |
| NO_MBB |
| NO_PSTN |
| NO_Bedrift |
| NO_TN_BB |
| NO_TN_TV |
| MAIN_PRODUCT_ID |
| NO_AGR_SWAP |

- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| MARKETING_NAME |
| MANUFACTURER |
| TOUCH_SCREEN |


