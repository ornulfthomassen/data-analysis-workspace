# VYA_GTIN_SAP_HERMES_RRP_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides historical and current recommended retail price (RRP) information, both ex-VAT and inc-VAT, for specific terminal device GTINs. It combines RRP data from SAP/Hermes retail articles with detailed product attributes such as manufacturer, model, color, and total size, sourced from a GTIN properties table. The view focuses on particular product categories (020102, 020101) and is intended for reporting in Viya.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.SAP_TN_WEB_RETL_ARTICLE_INFO]]
- ← [[FPS.TERMINAL_GTIN_PROPERTIES]]

