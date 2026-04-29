# HALO_DATAANALYSE_TMP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure initializes and populates a temporary customer data table (`clm_adm.tmp_GTT_SDU_KUNDER`) by extracting core customer and agreement details, and then iteratively enriches this data with derived attributes such as activation status, number of channels, loyalty programs, age, contract terms, and campaign participation, based on various related tables.

## Data Sources (Inputs)
- ← [[dual]]
- ← [[kas.avtale]]
| Column Name |
|---|
| abonnent_nr |
| status |
| produkt_nr |
| til_dato |
| fra_dato |
- ← [[kas.kunde]]
| Column Name |
|---|
| abonnent_nr |
| kundegruppe |
| kurt_id |
| hovedsentral |
| adresse_nr |
| notat2 |
| samband_nr |
| notat |
| fodselsdato |
- ← [[kas.samband]]
| Column Name |
|---|
| adresse_nr |
| bolig_nr |
| samband_nr |
| IP_RF_TV |
| type_CPE |
- ← [[bolig]]
| Column Name |
|---|
| adresse_nr |
| bolig_nr |
- ← [[clm_adm.tmp_GTT_SDU_KUNDER]]
| Column Name |
|---|
| abonnent_nr |
- ← [[kas.avtale_properties]]
| Column Name |
|---|
| abonnent_nr |
| tom_dato |
- ← [[cpm_produkt]]
| Column Name |
|---|
| produkt_nr |
| cpm_bibliotek_recno |
- ← [[cpm_bibliotek]]
| Column Name |
|---|
| cpm_recno |
| cpm_kategori |
| cpm_gyldig_tom |

## Target Tables (Outputs)
- → [[clm_adm.tmp_GTT_SDU_KUNDER]]
| Column Name |
|---|
| abonnent_nr |
| kundegruppe |
| kurt_id |
| kunde_konsept |
| aksess_teknologi |
| start_dato |
| epost |
| startoppsett |
| antall_lineære_kanaler |
| antall_poengpakker |
| kunde_alder |
| bindingstid |
| kampanje |

