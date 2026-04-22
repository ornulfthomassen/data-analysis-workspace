# V_IMEI_LIVE_EURKA

**Schema:** `CCM` | **Type:** `View`

## Description
Retrieves the most recent active usage details for specific mobile telephony subscription-based IMEI devices. For each qualifying IMEI, it extracts its identifier, a derived device key (likely the Type Allocation Code - TAC), the first and last dates of use, the associated customer key, product description, and product start/end dates. The selection is filtered for recent activity (terminal usage within the last 185 days), usage duration (more than 1 day), active subscriptions (prim_prod_end_dt_key = 99991231), and specific product classifications ('Tale', 'Abonnement', 'Mobil Telefoni'). If multiple usage records exist for an IMEI, the view selects the one with the latest terminal use dates.

## Data Sources (Inputs)
- ← [[live.eureka_imei]]
- ← [[galaxy.subscr_detail_fact]]
- ← [[galaxy.primary_product_dim_v]]
- ← [[clm_adm.adm_customer_mapping]]

