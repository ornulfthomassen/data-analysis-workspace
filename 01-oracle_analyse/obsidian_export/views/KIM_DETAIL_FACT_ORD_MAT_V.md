# KIM_DETAIL_FACT_ORD_MAT_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive, denormalized dataset for analyzing detailed campaign and marketing treatment outcomes. It focuses specifically on activities that resulted in new sales or product changes for customer subscriptions. The view combines core campaign facts with extensive details from various dimensions, including customer demographics, contact information, product attributes (for up to four products per treatment), treatment characteristics, channel used, and customer response details.

## Data Sources (Inputs)
- ← [[KIM_CAMPAIGN_DETAIL_FACT]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT_EXT]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[CRM_ANALYSE.KIM_CUSTOMER_RESPONSE]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_DIM]]
- ← [[CRM_ANALYSE.KIM_TREATMENT_PRODUCT_DIM_V]]
- ← [[CRM_ANALYSE.KIM_CHANNEL_DIM]]
- ← [[CRM_ANALYSE.KIM_RESPONSE_DIM]]

