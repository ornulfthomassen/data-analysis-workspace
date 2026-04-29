# VYA_INSIGHT_DEVICE_FROM_TB

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of Telenorbutikken device sales, enriching sales data with product group hierarchy, customer subscription details, and dealer information, primarily for analytical insights and loading into Viya.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MATERIAL_GROUPS_STAGE]]
| Column Name |
|---|
| VAREGRUPPE |
| BETEGNELSE_PAY_VAREGRUPPE |
| PARENT |
- ← [[THIRD_PARTY_SERVICES.T_BUTIKKEN_DEVICES]]
| Column Name |
|---|
| SERIENUMMER |
| FAKTURADATO |
| FILIAL |
| NAVN_PAY_FILIAL |
| ARTIKKEL |
| ARTIKKELKORTTEKST |
| VAREGRUPPE |
| BETEGNELSE_PAY_VAREGRUPPE |
| PRODUSENT |
| TELEFONNUMMER |
| BESTILLINGSNUMMER |
| OPPRETTELSESDATO |
| FAKTURATYPE |
- ← [[CLM_ADM.ADM_SUBSCRIPTION_MASTER_HIST]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER_SK |
| MAIN_NUMBER |
| ORIGINAL_START_DATE |
| END_DATE |
- ← [[GALAXY.DEALER_DIM]]
| Column Name |
|---|
| DEALER_KEY |
| SOURCE_DEALER_ID |
| START_DT_KEY |
| END_DT_KEY |

