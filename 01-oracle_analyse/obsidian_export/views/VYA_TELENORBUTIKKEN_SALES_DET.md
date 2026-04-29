# VYA_TELENORBUTIKKEN_SALES_DET

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides detailed and enriched sales data for 'Telenorbutikken' for loading into Viya. It combines raw sales transaction data with hierarchical product group information, salesperson details (including anonymization for less active salespersons), and customer/salesperson subscription keys from historical subscription master data.

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
| NAVN_PAY_FILIAL |
| ORDRENUMMER |
| ORDREPOSISJON |
| BONG_ID |
| ARTIKKEL |
| GAMMELT_ARTIKKELNR |
| ARTIKKELKORTTEKST |
| KVANTUM |
| SALGSKVANTUMSENHET |
| VAREGRUPPE |
| NETTOVERDI |
| AVREGNINGSPRIS |
| PROVISJONER |
| TAP_PAY_FORDRINGER |
| TERMINALSTATTE |
| DEKNINGSBIDRAG |
| VALUTA |
| KUNDENUMMER |
| KUNDENAVN |
| SERIENUMMER |
| PRODUSENT |
| BESTILLINGSNUMMER |
| RUN_ID |
| SELGER |
| SELGERNAVN |
| TELEFONNUMMER |
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
| Column Name |
|---|
| VAREGRUPPE |
| PARENT |
| BETEGNELSE_PAY_VAREGRUPPE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| ORIGINAL_START_DATE |
| MAIN_NUMBER |
| END_DATE |
| MAIN_NUMBER_SK |

