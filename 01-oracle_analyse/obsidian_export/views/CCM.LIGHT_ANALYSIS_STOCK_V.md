# LIGHT_ANALYSIS_STOCK_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive analytical dataset by consolidating subscription, product, customer (both user and owner), household, address, and device information. It focuses on top-level subscriptions, integrating key performance indicators, demographic details, product attributes, and device specifications for detailed analytical reporting, often used in CRM or business intelligence contexts.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PARENT_SUBSCRIPTION_ID |
| MAIN_NUMBER |
| USER_KURT_ID |
| OWNER_KURT_ID |
| MAIN_PRODUCT_ID |
| SUBSCRIPTION_TYPE |
| END_DATE |
| START_DATE |
| ORIGINAL_START_DATE |
| PAYMENT_METHOD_ID |
| DEVICE_TAC |

- ← [[CLM_CCM.CCM_SUBSCRIPTION_INFO_2]]
| Column Name |
|---|
| SUBSCRIPTION_ID |

- ← [[CLM_CCM.CCM_PRODUCT_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_ID |

- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| AGE |
| GENDER |
| CUSTOMER_STATUS_CD |
| HOUSEHOLD_ID |

- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2]]
| Column Name |
|---|
| KURT_ID |
| CLM_LIVSFASE_SEGMENT_NAME |
| MAP_SEGMENT_NAME |
| CU_NO_FBB_COAX |
| CU_NO_FBB_FBR_FTV |
| CU_NO_MPP |
| CU_NO_MPP_USR |
| CU_NO_MPR |

- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| FARID |

- ← [[CLM_CCM.CCM_FAR]]
| Column Name |
|---|
| FARID |
| MUNICIPALITY_CODE |
| MUNICIPALITY_NAME |
| STREETPOSTALADDRESS |
| STREETPOSTALCODE |

- ← [[GALAXY.PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_FAMILY_NAME |
| DRM_COMMON_PORTFOLIO |
| PRODUCT_NAME |
| DRM_COMMON_PRODUCT_AREA |
| DRM_COMMON_PRODUCT_GROUP |
| DRM_COMMON_REPORTING |
| DRM_COMMON_PAYMENT |
| MONTHLY_PRICE |
| SOURCE_PRODUCT_ID_1 |
| INCLUDED_DATA |

- ← [[GALAXY.HANDSET_DIM_V]]
| Column Name |
|---|
| HANDSET_KEY |
| CAMERA_INFO |
| HANDSET_TYPE |
| MANUFACTURER |
| MARKETING_NAME |
| OS_INFO |
| LTE |
| UMTS |
| HSDPA |
| GPRS |
| EDGE |


