# HALO_DATAANALYSE_TMP

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure initializes and then iteratively enriches a temporary Global Temporary Table (GTT) named 'clm_adm.tmp_GTT_SDU_KUNDER'. It starts by inserting subscriber and customer base data, then fetches and updates additional attributes such as access technology, setup status, number of linear channels, 'point packages', customer age, contract binding status, and campaign participation. This consolidation of customer/subscriber-related information from various source tables into a single temporary structure is likely for further analysis, reporting, or as an intermediate step for other processes.

## Data Sources (Inputs)
- ← [[dual]]
- ← [[kas.avtale]]
- ← [[kas.kunde]]
- ← [[kas.samband]]
- ← [[kas.bolig]]
- ← [[kas.avtale_properties]]
- ← [[cpm_produkt]]
- ← [[cpm_bibliotek]]

## Target Tables (Outputs)
- → [[clm_adm.tmp_GTT_SDU_KUNDER]]

