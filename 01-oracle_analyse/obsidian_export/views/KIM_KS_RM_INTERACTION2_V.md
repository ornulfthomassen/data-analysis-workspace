# KIM_KS_RM_INTERACTION2_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a comprehensive dataset for customer interactions, consolidating detailed interaction segments, temporal information, call center performance metrics, customer identifiers, and customer satisfaction (CSAT) survey results. It includes various duration and count metrics related to customer handling, waiting, talking, and IVR/manual callbacks, along with service level agreement (SLA) indicators. Employee IDs are hashed for privacy. It acts as a central source for analyzing and reporting on customer interaction data.

## Data Sources (Inputs)
- ← [[RSSHUGIN.RM_KS_INTERACTION]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[CCDW_CUSTOMER_EVENT.SURVEY_RESPONSE_FACT]]

