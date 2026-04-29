# ADM03_ADDR_COVERAGE_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Manages the historical address coverage data. It first ensures the `CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST` table exists, creating it with specified columns and partitioning if necessary. It then checks if the previous month's data (derived from SYSDATE) has already been loaded. If not, it adds a new partition for that month to the `ADM_ADDR_COVERAGE_HIST` table and populates it with detailed coverage information from the `CLM_CCM.CCM_COVERAGE_NEW` table. The procedure also gathers statistics and logs its activities.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |
| SUBOBJECT_NAME |
- ← [[DUAL]]
- ← [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[CLM_CCM.CCM_COVERAGE_NEW]]
| Column Name |
|---|
| FARID |
| GAB_NUMBER |
| FT_POTS_OK_RESULT |
| FB_KAPAKS_FLG |
| FB_GSL |
| FB_LINE_STATUS |
| FB_LINE_USAGE_CATEGORY |
| FB_ADSL_MAX_DOWNLOAD_SPEED |
| FB_ADSL_MAX_PRODUCT_CLASS_CODE |
| FB_ADSL_MAX_PRODUCT_CLASS_TEXT |
| FB_ADSL_OK_RESULT |
| FB_ADSL_RESULT_CODE |
| FB_VDSL_MAX_DOWNLOAD_SPEED |
| FB_VDSL_MAX_PRODUCT_CLASS_CODE |
| FB_VDSL_MAX_PRODUCT_CLASS_TEXT |
| FB_VDSL_OK_RESULT |
| FB_VDSL_RESULT_CODE |
| FB_SOURCE_SYSTEM |
| FB_METHOD |
| MB_FAR_COVERAGE_FLG |
| MB_QUALITY_2G |
| MB_QUALITY_4G_PLUS |
| MB_QUALITY_4G |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_ADDR_COVERAGE_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| FARID |
| GAB_NUMBER |
| POTS_OK_RESULT |
| KAPAKS_FLG |
| GSL |
| LINE_STATUS |
| LINE_USAGE_CATEGORY |
| ADSL_MAX_DOWNLOAD_SPEED |
| ADSL_MAX_PRODUCT_CLASS_CODE |
| ADSL_MAX_PRODUCT_CLASS_TEXT |
| ADSL_OK_RESULT |
| ADSL_RESULT_CODE |
| VDSL_MAX_DOWNLOAD_SPEED |
| VDSL_MAX_PRODUCT_CLASS_CODE |
| VDSL_MAX_PRODUCT_CLASS_TEXT |
| VDSL_OK_RESULT |
| VDSL_RESULT_CODE |
| SOURCE_SYSTEM |
| METHOD |
| FAR_COVERAGE_FLG |
| GSM_IN |
| GSM_OUT |
| LTE_IN |
| LTE_OUT |

