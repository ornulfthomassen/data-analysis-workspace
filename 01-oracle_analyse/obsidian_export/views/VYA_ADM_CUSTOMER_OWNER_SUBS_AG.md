# VYA_ADM_CUSTOMER_OWNER_SUBS_AG

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates monthly subscription and financial data (gross/net fees) for customers identified as 'owners'. It calculates the number of subscriptions for various product categories such as mobile postpaid (MPP), mobile prepaid (MPR), mobile broadband (MBB), fixed line (FIX), DSL, and fiber (FBR). It also determines the total number of distinct product categories a customer owner subscribes to and the total number of subscriptions (TNM + DJU). The view combines monthly period information with customer-specific aggregated subscription details, likely for loading into a data mart named 'Mjøsa' as indicated in the comments.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_CUSTOMER_OWNER_SUBS_AGG]]
- ← [[CLM_ADM.ADM_MONTH_DIM]]

