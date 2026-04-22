# KIM_KS_IVR_DIALOG_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, 'KIM_KS_IVR_DIALOG_V', provides a consolidated and enriched dataset of Interactive Voice Response (IVR) dialogue interactions. It combines core IVR session details (such as start time, connection ID, service path, called service, technical results, and service flow) with customer-related information by mapping owner and user IDs to customer surrogate keys. Additionally, it integrates customer satisfaction (CSAT) scores for specific questions from survey data. The view also derives various temporal attributes (date, year-month, year-week numbers) and customizes service names/types based on the interaction's nature (e.g., 'Queuing'), making the data suitable for comprehensive analysis of IVR performance, customer journey, and satisfaction.

## Data Sources (Inputs)
- ← [[RSSHUGIN.IVR_DIALOG]]
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

