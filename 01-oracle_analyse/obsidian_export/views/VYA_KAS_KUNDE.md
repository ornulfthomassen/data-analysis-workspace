# VYA_KAS_KUNDE

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'VYA_KAS_KUNDE', provides a comprehensive and consolidated view of customer data. It primarily draws information from the 'KAS.KUNDE' table, enriching and transforming it by integrating customer mapping details from 'CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V'. The view includes various customer attributes such as name, unique identifiers, address components, financial status (saldo, credit limit), contract details, and multiple status flags. It performs data transformations like case conversion, date formatting, and conditional logic for generating customer names and unique keys, while also filtering out specific customer types.

## Data Sources (Inputs)
- ← [[KAS.KUNDE]]
| Column Name |
|---|
| ABONNENT_NR |
| KOLL_ID |
| ETTERNAVN |
| KURT_ID |
| ADRESSE_NR |
| POST_NR |
| ANL_ADRESSE |
| HUS_NR |
| OPPGANG |
| LEILIGHET_NR |
| NOTAT2 |
| ETASJE |
| SALDO |
| NETT_NR |
| KUNDE_TYPE |
| SUB_KUNDE |
| ANSVARSTED |
| KABEL_ADR_OK |
| STOP_KODE |
| BOLIG_TYPE |
| KONTRAKT_TYPE |
| ANTALL |
| ANTALL_ROM |
| HOVEDSENTRAL |
| FORETAKSNR |
| KONTRAKTSNR |
| BET_MAATE |
| KREDITTGRENSE |
| REGNSKAPS_TYPE |
| MVA_KODE |
| BET_BETINGELSE |
| KUNDEGRUPPE |
| KUNDE_STATUS_TILSTAND |
| DATO_STATUS_TILSTAND |
| KUNDE_STATUS_PROSESS |
| DATO_STATUS_PROSESS |
| KONTRAKT_DATO |
| REG_DATO |
| TILKOBLET_DATO |
| OPPSAGT_DATO |
| STENGT_DATO |
| TEKNISK_REF |
| NETT_TYPE |
| SERIENETT_NR |
| PURRES |
| KAN_STENGES |
| STENGES |
| FAKTURA_GEBYR |
| SPESIFIKASJONS_NIVAA |
| SPRAAK_KODE |
| KLUBB_KONTO |
| ENDRET_DATO |
| FODSELSDATO_DATO |
| KUNDE_KILDE |
| TYPE_UTSENDELSE |
| SUPERNODE |
| EFAKTURA |
| SAMBAND_NR |
| SAMLE_FAKTURA |
| SAMLE_FAKTURA_TERMIN |
| EHF_FAKTURA |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_KEY |

