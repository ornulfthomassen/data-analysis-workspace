# P_SU_ODS_SUB_CAMPAIGN_OFFER_FTV

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure implements a dynamic table refresh and swap mechanism for the `ODS_SUB_CAMPAIGN_OFFER_FTV` table. It loads new data into a temporary table (`ODS_SUB_CAMPAIGN_OFFER_FTV_N`), creates necessary indexes on it, and then conditionally replaces the main target table (`ODS_SUB_CAMPAIGN_OFFER_FTV`) with the newly populated temporary table. The old version of the main table is retained as a backup (`ODS_SUB_CAMPAIGN_OFFER_FTV_O`). The swap is performed based on a configurable percentage deviation (`V_RANGE_SWAP`) between the row counts of the new data and the existing main table. It includes robust logging and error handling for the swap operations.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| SOURCE_SYSTEM_ID |
| SOURCE_SYSTEM_KEY_2 |

- ← [[KAS.KM_ORDREHODE]]
| Column Name |
|---|
| RECNO |
| ABONNENT_NR |
| KANAL |
| TILBUD_ID |
| REG_DATO |
| EXTREF |
| ORDRE_ID |

- ← [[KAS.AVTALE]]
| Column Name |
|---|
| KM_RECNO |
| ABONNENT_NR |
| PRODUKT_NR |
| BINDINGSTID_DATO |
| PRIS_ENDRINGSDATO |
| FAKT_DATO |
| FAKT_TOM |
| FRA_DATO |
| TIL_DATO |
| status |

- ← [[KASSO.OFFER_CONFIG]]
| Column Name |
|---|
| OFFERID |
| NAME |
| CAMPAIGNTYPE |
| HASBINDING |
| MONTHLYDISCOUNTLENGTH |
| TOTALRECURRINGPRICE |


## Target Tables (Outputs)
- → [[CCM.ODS_SUB_CAMPAIGN_OFFER_FTV]]
| Column Name |
|---|
| LOAD_DTTM |
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| ABONNENT_NR |
| EXTERNAL_ORDER_REF_ID |
| ORDER_REG_DATE |
| ORDER_ID |
| CAMPAIGN_OFFER_ID |
| CHANNEL |
| OFFER_NAME |
| CAMPAIGN_TYPE |
| BINDING_FLAG |
| OFFER_DISCOUNT_PERIOD_MONTHS |
| CAMPAIGN_DISCOUNT_PERIOD |
| OFFER_PRICE |
| BINDING_END_DATE |
| CAMPAIGN_DISCOUNT_END_DATE |
| PRICE_CHANGE_DATE |
| INVOICE_DATE |
| NEXT_INVOICE_DATE |
| LAST_CAMPAIGN_FLAG |
| LAST_FLAG |
| CAMPAIGN_DISCOUNT_START_DATE |
| CAMPAIGN_NEWSALE_AREA |
| CAMPAIGN_STATUS_KAS |

- → [[CCM.ODS_SUB_CAMPAIGN_OFFER_FTV_N]]
| Column Name |
|---|
| LOAD_DTTM |
| SUBSCRIPTION_ID |
| SOURCE_SYSTEM_KEY |
| ABONNENT_NR |
| EXTERNAL_ORDER_REF_ID |
| ORDER_REG_DATE |
| ORDER_ID |
| CAMPAIGN_OFFER_ID |
| CHANNEL |
| OFFER_NAME |
| CAMPAIGN_TYPE |
| BINDING_FLAG |
| OFFER_DISCOUNT_PERIOD_MONTHS |
| CAMPAIGN_DISCOUNT_PERIOD |
| OFFER_PRICE |
| BINDING_END_DATE |
| CAMPAIGN_DISCOUNT_END_DATE |
| PRICE_CHANGE_DATE |
| INVOICE_DATE |
| NEXT_INVOICE_DATE |
| LAST_CAMPAIGN_FLAG |
| LAST_FLAG |
| CAMPAIGN_DISCOUNT_START_DATE |
| CAMPAIGN_NEWSALE_AREA |
| CAMPAIGN_STATUS_KAS |

- → [[CCM.ODS_SUB_CAMPAIGN_OFFER_FTV_O]]
- → [[CCM.ODS_SUB_CAMPAIGN_OFFER_FTV_OT]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]
| Column Name |
|---|
| PROC_NAME |
| LOG_DTTM |
| MESSAGE |
| OLD_ROW_COUNT |
| NEW_ROW_COUNT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| LOG_LEVEL |
| MESSAGE |
| POWERCENTER_WF_NAME |
| POWERCENTER_S_NAME |


