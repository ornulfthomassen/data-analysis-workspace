# GCP_HOUSEHOLD_DEMOGRAPHICS_AGG

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates detailed demographic, service penetration (fixed and mobile), network coverage, and geographical/property characteristics for households. It provides insights into household composition (age, gender, predicted children), communication preferences, fixed broadband (FBB) and fixed wireless access (FWA) availability, competitor presence, and various service usage statistics.

## Data Sources (Inputs)
- ← [[CLM_FIXED_ADM.FTV_ADM_ADDRESS]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO_V]]
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
- ← [[CLM_CCM.CCM_CUSTOMER_INFO_2_V]]
- ← [[CLM_CCM.ODS_FAR]]
- ← [[CCDW_CTI.CTI_CONS_HOUSEHOLD]]
- ← [[CLM_ADM.MUNICIPALITY_COUNTY_REGION_DIM]]
- ← [[CLM_CCM.HH_CHILD_PROBABILITY]]
- ← [[CLM_CCM.ODS_COVERAGE]]
- ← [[FAR.ADDRESS_PROPERTIES]]
- ← [[CLM_FIXED_CCM.FTV_CCM_FAR_ADR_NKOM_ISP]]
- ← [[CLM_FIXED_ADM.FTV_ADM_ADDRESS_COMPETITION]]

