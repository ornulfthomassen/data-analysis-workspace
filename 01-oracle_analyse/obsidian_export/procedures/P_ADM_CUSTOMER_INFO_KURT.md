# P_ADM_CUSTOMER_INFO_KURT

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure (`P_ADM_CUSTOMER_INFO_KURT`) is designed to create or refresh a comprehensive customer information table named `ADM_CUSTOMER_INFO_KURT`. It aggregates and enriches customer-related data, including personal details, household information, contact addresses, and service subscriptions, from various operational data store (ODS) and data warehouse (DWH) sources. The procedure first performs a data quality/freshness check on its primary source tables for the previous month. It then implements a table rotation strategy: if an old backup table (`ADM_CUSTOMER_INFO_KURT_OLD`) exists and is outdated or an overwrite is explicitly requested, it is dropped. The current `ADM_CUSTOMER_INFO_KURT` table is then renamed to `ADM_CUSTOMER_INFO_KURT_OLD` to serve as a backup, and a new `ADM_CUSTOMER_INFO_KURT` table is created using a `CREATE TABLE AS SELECT` statement. Finally, statistics are gathered on the newly created table.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MONTH_DIM]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| NEXT_PERIOD_MONTH_KEY |
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| LOAD_DTTM |
- ← [[CLM_CCM.CCM_CUST_CONTACT_ADDRESS_V]]
| Column Name |
|---|
| LOAD_DTTM |
| KURT_ID |
| POSTCODE_ID |
| POSTCODE_NAME |
- ← [[ADM_CUSTOMER_INFO_KURT_OLD]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| HOUSEHOLD_ID |
| DATE_OF_BIRTH |
| CUSTOMER_AGE |
| CUSTOMER_TYPE_ID |
| CUSTOMER_STATUS_ID |
- ← [[CCDW.CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| GENDER |
- ← [[ODS.CUSTOMER_RES_AND_APP]]
| Column Name |
|---|
| CUSTOMER_ID |
| TM_IND_BR |
| DM_IND_BR |
| TM_IND_INTERNAL |
| DM_IND_INTERNAL |
| EMAIL_IND |
| SMS_IND |
| EMAIL_ADDRESS |
| SMS_NUMBER |
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO_V]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FAR_ID |
| GAB_NUMBER |
| HOUSEHOLD_MEMBER_COUNT |
| BYGNINGSTYPE_ID |
| BOLIGTYPE |
| HH_NO_FIX_POTS_HH_ADR |
| HH_NO_FIX_POTS_BUS_HH_ADR |
| HH_NO_FIX_BBT_FTV_HH_ADR |
| HH_NO_FIX_BBT_TNN_HH_ADR |
| HH_NO_TV_FTV_HH_ADR |
| HH_NO_TV_FTV_UNKNOWN_ADR |
| HH_NO_FBB_DSL_HH_ADR |
| HH_NO_FBB_DSL_BUS_HH_ADR |
| HH_NO_FBB_FWA_BUS_HH_ADR |
| HH_NO_FBB_FWA_HH_ADR |
| HH_NO_FBB_FWA_UNKNOWN_ADR |
| HH_NO_FBB_FBR_FTV_HH_ADR |
| HH_NO_FBB_FBR_TNN_HH_ADR |
| HH_NO_FBB_FBR_FTV_UNKNOWN_ADR |
| HH_NO_MBB_USR |
| HH_NO_MBB_BUS_USR |
| HH_NO_MPP_USR |
| HH_NO_MPP_BUS_USR |
| HH_NO_MPR_USR |
| HH_NO_FIX_POTS_OTHER_ADR |
| HH_NO_FIX_POTS_BUS_OTHER_ADR |
| HH_NO_TV_FTV_OTHER_ADR |
| HH_NO_FBB_DSL_OTHER_ADR |
| HH_NO_FBB_FWA_UNKNOWN_ADR |
| HH_NO_FBB_FBR_FTV_OTHER_ADR |
| HH_NO_FBB_FBR_TNN_OTHER_ADR |
| HH_NO_DSL_ISP_LINES |
| HH_NO_MOB_OTHER_SP |
- ← [[CLM_CCM.CCM_FAR_V]]
| Column Name |
|---|
| FARID |
| STREETPOSTALCODE |
| STREETPOSTALADDRESS |
| MUNICIPALITY_CODE |
| BASIC_STATISTICAL_UNIT_ID |
| BASIC_STATISTICAL_UNIT_NAME |
| CO_OPERATIVE_HOUSING_ID |
| FLATNUMBER |
| ADDRESS_TYPE |
| ADDRESS_STATUS |
- ← [[CCDW.ADDRESS_TYPE]]
| Column Name |
|---|
| ADDRESS_TYPE_ID |
| ADDRESS_TYPE_DESC |
- ← [[CCDW.ADDRESS_STATUS]]
| Column Name |
|---|
| ADDRESS_STATUS_DESC |

## Target Tables (Outputs)
- → [[ADM_CUSTOMER_INFO_KURT]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| KURT_ID |
| HOUSEHOLD_ID |
| DATE_OF_BIRTH |
| AGE |
| GENDER |
| EMAIL_IND |
| SMS_IND |
| EMAIL_ADRESSE_FLAG |
| SMS_MOBIL_FLAG |
| RES_BRSUND_TM |
| RES_BRSUND_DM |
| RES_TELENOR_TM |
| RES_TELENOR_DM |
| CUSTOMER_TYPE_CD |
| CUSTOMER_STATUS_CD |
| FARID |
| GAB_NUMBER |
| ANTALL_I_HUSSTAND |
| POSTADR_POSTNR |
| POSTADR_POSTSTED |
| POSTNR |
| POSTSTED |
| CU_HH_SAME_ADDR_FLAG |
| KOMMUNENR |
| GRUNNKRETS_NR |
| GRUNNKRETS |
| BORETTSLAGSID |
| BYGNINGSTYPE_NR |
| BOLIGTYPE |
| LEILIGHET_NR |
| ADRESSETYPE |
| ADRESSESTATUS |
| FIXED_TALE |
| TV |
| FIXED_INTERNETT_DSL |
| FIXED_INTERNETT_TBB |
| FIXED_INTERNETT_FIBER |
| MOBIL_INTERNETT |
| MOBIL_TALE |
| FIXED_TALE_UTENF_HS |
| TV_UTENF_HS |
| FIXED_INTERNETT_DSL_UTENF_HS |
| FIXED_INTERNETT_TBB_UTENF_HS |
| FIXED_INTERNETT_FIBER_UTENF_HS |
| MULIG_ADSL_HOS_ANDRE |
| MOBIL_TALE_HOS_ANDRE |
- → [[ADM_CUSTOMER_INFO_KURT_OLD]]

