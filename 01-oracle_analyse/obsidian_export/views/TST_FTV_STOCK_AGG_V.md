# TST_FTV_STOCK_AGG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and calculates key performance indicators (KPIs) related to product stock, customer base changes, and product transitions over time. It computes opening and closing balances for various product combinations (Broadband, TV, Dualplay, BB Only, TV Only) and tracks detailed net changes, 'tilvekst' (growth/additions), and 'churn' (losses/disconnections). The view categorizes these changes by factors like network type (offnet, onnet), customer movement (flytting, return), competition (konkurrent), and technical changes (speed increase/decrease, technology change, product change, subtype change, crossover to fiber). It enriches the stock data with product attributes such as name, POID, area, group, reporting, dwelling unit type, category, technology, and speed, providing a comprehensive temporal view of the product portfolio and customer base dynamics.

## Data Sources (Inputs)
- ← [[CCM.TST_FTV_STOCK_BASE]]
- ← [[CCM.FTV_PRODUCT_BB_V_TMP]]
- ← [[GALAXY.DATE_DIM_MV]]

