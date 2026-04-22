# ORDER_LINE_DETAIL_MOB_ENRICH_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view provides an enriched and comprehensive dataset of mobile order line details, incorporating various dimensions and calculating key performance indicators (KPIs). It specifically focuses on mobile telecommunications by filtering on a specific business area (Mobile), market areas, and source systems, and only includes recent order activity from the beginning of the previous year. The view enriches order line data with product details (from and to products), sales matrix categorization, device swapping information, regret order details, customer segmentation (MAP2, CLMLS), and mobile agreement product details (e.g., for data bonuses). It calculates specific KPIs for newsales, porting, terminations, and gross sales, often differentiating between 'Speech' (Mobil Telefoni) and 'MBB' (Mobil Bredbånd/Datakort) product areas, serving as a consolidated analytical layer for mobile order line activities.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.ORDER_LINE_PRODUCT_DIM_V]]
- ← [[GALAXY.FROM_ORDER_PRODUCT_DIM_V]]
- ← [[GALAXY.ORDER_NEWSALE_SWAP_V]]
- ← [[GALAXY.ORDER_LINE_DETAIL_MOB_REGRET_V]]
- ← [[CCDW_SEGMENT.CUSTOMER_SEGMENT_V]]
- ← [[GALAXY.SEGMENT_DIM]]
- ← [[CCDW.DEVICE_AGREE_SWAPPING_MV]]
- ← [[CCDW.AGREEMENT_PRODUCT_MOB_SD_MV]]

