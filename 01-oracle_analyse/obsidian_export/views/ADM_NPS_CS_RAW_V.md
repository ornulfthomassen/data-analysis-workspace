# ADM_NPS_CS_RAW_V

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view is designed to consolidate and standardize Net Promoter Score (NPS) survey data with customer subscription history and mobile number porting information. Its main purpose is to extract raw NPS survey responses, cleanse and transform them (especially the NPS score and category from various input formats), and enrich them with details such as customer identifiers, transaction dates, call center metrics (topic, time in queue, conversation time), customer demographics, and porting status. It aims to provide a comprehensive dataset for NPS analysis.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[NPS.MEDALLIA_SURVEY_IMPORT]]
- ← [[CRM_ANALYSE.ADM_MOBIL_SUBSCR_HIST]]
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT]]
- ← [[CRM_ANALYSE.MPORT_PORT_REPORT_EXTRA_INFO]]

