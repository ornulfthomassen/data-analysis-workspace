# KIM_UPD_SALES_MATRIX

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through records in the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table where ORDER_MATCH_KEY is positive, SALES_MATRIX is NULL, CONTACT_DATE_KEY is recent (>= 20140101), and MEASURE_TYPE is 1. For each such record, it calculates a 'SALES_MATRIX' value (Newsale, Upsale, Downsale, Neutrale, or Error) based on product type configurations from CLM_CCM.CCM_PRODUCT_TYPE_CONFIG and various KPI flags (KPI_NEWSALE, KPI_PRODUCT_CHANGE). Finally, it updates the SALES_MATRIX column in the CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT table for the corresponding records, committing changes in batches of 10,000.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| SOURCE_SYSTEM_KEY |
| KPI_NEWSALE |
| KPI_PRODUCT_CHANGE |
| ORDER_TO_PRODUCT_KEY |
| ORDER_FROM_PRODUCT_KEY |
| ORDER_MATCH_KEY |
| SALES_MATRIX |
| CONTACT_DATE_KEY |
| MEASURE_TYPE |
- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| H_LEVEL |
| SORT_ORDER |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| SALES_MATRIX |

