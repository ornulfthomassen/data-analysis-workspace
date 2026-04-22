# VYA_SUBSCR_OUTPORT

**Schema:** `CCM` | **Type:** `View`

## Description
Identifies and lists future or pending outbound mobile phone subscription porting requests. It provides details such as the subscription key, the specific mobile telephony product being ported, the agreed porting date, the destination service provider, and an outbound porting KPI. The view specifically filters for 'open' (active/pending) porting orders in designated market areas.

## Data Sources (Inputs)
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[GALAXY.MARKET_AREA_DIM]]
- ← [[GALAXY.ORDER_STATUS_DIM_MV]]

