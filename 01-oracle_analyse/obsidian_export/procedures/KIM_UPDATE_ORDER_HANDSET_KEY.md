# KIM_UPDATE_ORDER_HANDSET_KEY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure iterates through specific campaign detail records (`CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT`) that meet certain criteria and are joined with order line details (`galaxy.order_line_detail_fact_mv`). For each matching record, it updates the `ORDER_HANDSET_KEY` column in the `CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT` table, setting it to the `HANDSET_KEY` obtained from the corresponding order line detail record. Updates are committed in batches of 10,000 records.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| CONTACT_KEY |
| ORDER_ID |
| ORDER_MATCH_KEY |
| ORDER_HANDSET_KEY |
| BINDING_BENEFIT_DESC |
| CONTACT_DATE_KEY |
- ← [[galaxy.order_line_detail_fact_mv]]
| Column Name |
|---|
| HANDSET_KEY |
| SOURCE_ORDER_ID |
| BUSINESS_AREA_KEY |
| MARKET_AREA_KEY |

## Target Tables (Outputs)
- → [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| ORDER_HANDSET_KEY |

