# VYA_ODS_AGREEMENT_DEVICE

**Schema:** `CCM` | **Type:** `View`

## Description
This view, VYA_ODS_AGREEMENT_DEVICE, extracts and consolidates comprehensive data about active agreement devices. It combines information from agreement offers, product details, customer mappings, and device dimensions. The purpose is to provide a unified dataset for analytical use in an Operational Data Store (ODS), likely for systems like SAS Viya. It enriches agreement records with product attributes, device specifications (derived from IMEI), customer ownership, and calculates various date-related metrics such as product active days. It filters for active products and performs data cleaning and transformation on device identifiers (IMEI) and names.

## Data Sources (Inputs)
- ← [[CLM_CCM.V_ODS_AGRMT_OFFER_MOB_DEVICE]]
- ← [[CRM_ANALYSE.PD]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CLM_ADM.ADM_DEVICE_DIM]]
- ← [[GALAXY.ORDER_LINE_DETAIL_FACT_MV]]
- ← [[CLM_ADM.ADM_DEVICE_RANGE_DIM]]

