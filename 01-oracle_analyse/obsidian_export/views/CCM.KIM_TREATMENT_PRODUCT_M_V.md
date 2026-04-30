# KIM_TREATMENT_PRODUCT_M_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates and enriches 'treatment' data from multiple source tables. It joins core treatment information with extended attributes, character user-defined fields, and up to four related product configurations. The view calculates and assigns various categorization fields like KPI type, action category, and offer category based on complex business logic, providing a comprehensive view of treatments and their associated product details.

## Data Sources (Inputs)
- ← [[CLM_CDM.CI_TREATMENT]]
| Column Name |
|---|
| TREATMENT_SK |
| TREATMENT_CD |
| TREATMENT_NM |
| TREATMENT_DESC |
| CURRENT_VERSION_FLG |
| TREATMENT_REFERENCE_TXT |
| TREATMENT_REFERENCE_URL |
| DELETED_FLG |
| PROCESSED_DTTM |
| TREATMENT_VERSION_NO |

- ← [[CLM_CDM.CI_TREATMENT_EXT]]
| Column Name |
|---|
| TREATMENT_SK |
| BRAND |
| ACTION_CATEGORY |
| KPI_PRODUCT_CHANGE |
| KPI_NEWSALE |
| PRODUCT_ID1 |
| PRODUCT_ID2 |
| PRODUCT_ID3 |
| PRODUCT_ID4 |
| OFFER_CATEGORY |
| EXPECTED_VALUE |
| FH_VALID_FROM_DATE |
| FH_VALID_TO_DATE |
| TM_VALID_FROM_DATE |
| TM_VALID_TO_DATE |
| KS_VALID_FROM_DATE |
| KS_VALID_TO_DATE |
| MS_VALID_FROM_DATE |
| MS_VALID_TO_DATE |
| MT_VALID_FROM_DATE |
| MT_VALID_TO_DATE |

- ← [[CLM_CDM.CI_TREATMENT_CHAR_UDF]]
| Column Name |
|---|
| TREATMENT_SK |
| CHAR_UDF_NM |
| TREATMENT_HASH_VAL |
| CHAR_UDF_VAL |
| CHAR_EXT_COLUMN_NM |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| DESCRIPTION |
| VALUE |
| SUBSTITUTION_PROD_ID1 |


