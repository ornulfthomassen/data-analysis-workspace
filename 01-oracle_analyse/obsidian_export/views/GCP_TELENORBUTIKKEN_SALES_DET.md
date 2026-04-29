# GCP_TELENORBUTIKKEN_SALES_DET

**Schema:** `CCM` | **Type:** `View`

## Description
This view processes and enriches raw Telenorbutikken sales transaction data, including quantity and value adjustments for returns, hierarchical product group categorization, dealer information, and subscription details for both sellers and customers. It filters for recent sales records (current and past two years) and prepares a detailed, consolidated sales dataset for GCP, including some data standardization and anonymization.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.T_BUTIKKEN_DEVICES]]
| Column Name |
|---|
| FAKTURA |
| FAKTURAPOSISJON |
| FAKTURADATO |
| OPPRETTELSESDATO |
| OPPRETTELSESTID |
| FAKTURATYPE |
| BETEGNELSE_PAY_FAKTURATYPE |
| FILIAL |
| ORDRENUMMER |
| ORDREPOSISJON |
| BONG_ID |
| ARTIKKEL |
| GAMMELT_ARTIKKELNR |
| ARTIKKELKORTTEKST |
| KVANTUM |
| SALGSKVANTUMSENHET |
| VAREGRUPPE |
| BETEGNELSE_PAY_VAREGRUPPE |
| NETTOVERDI |
| AVREGNINGSPRIS |
| TAP_PAY_FORDRINGER |
| TERMINALSTATTE |
| DEKNINGSBIDRAG |
| PROVISJONER |
| VALUTA |
| KUNDENUMMER |
| KUNDENAVN |
| SELGERNAVN |
| SELGER |
| SERIENUMMER |
| PRODUSENT |
| TELEFONNUMMER |
| BESTILLINGSNUMMER |
| RUN_ID |
| SEQ_ID |
| CCDW_LOAD_DATE |
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
| Column Name |
|---|
| VAREGRUPPE |
| BETEGNELSE_PAY_VAREGRUPPE |
| PARENT |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| SOURCE_DEALER_ID |
| START_DT_KEY |
| END_DT_KEY |
| DRM_SALES_CHANNEL_GEN07_DESC |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIGINAL_START_DATE |
| END_DATE |
| MAIN_NUMBER |
| MAIN_NUMBER_SK |

