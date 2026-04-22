# KS_INTERACTION_V_X

**Schema:** `CCM` | **Type:** `View`

## Description
This view, "KS_INTERACTION_V_X", serves as a comprehensive reporting layer for customer interactions, primarily focusing on a specific media type (likely calls, indicated by MEDIA_TYPE_KEY = 1). Its main purpose is to consolidate detailed interaction data from various staging and dimension tables, enriching it with organizational context (agent, team, unit, site, company), queue information (client, program, type), and extensive user-defined custom attributes. It calculates interaction start and end times, adjusts for daylight saving, and determines sequential interaction timing for agents (`START_Cal_Date_NEXT`) for performance analysis. The view is designed to provide a unified dataset suitable for advanced analysis, forecasting, and traffic reporting, especially concerning agent performance, interaction flow, and adherence to COPC (Customer Operations Performance Center) specifications.

## Data Sources (Inputs)
- ← [[KS_STAGING.INTERACTION_FACT]]
- ← [[CRM_ANALYSE.KS_INTERACTION_LOAD_LOG_V]]
- ← [[KS_STAGING.INTERACTION_RESOURCE_FACT]]
- ← [[KS_STAGING.MEDIATION_SEGMENT_FACT]]
- ← [[KS_STAGING.DATE_TIME]]
- ← [[RSSHUGIN.DIM_CALENDAR_WORKDAY]]
- ← [[KS_STAGING.INTERACTION_TYPE1]]
- ← [[KS_STAGING.MEDIA_TYPE]]
- ← [[KS_STAGING.RESOURCE_]]
- ← [[KS_STAGING.TECHNICAL_DESCRIPTOR]]
- ← [[KS_STAGING.IRF_USER_DATA_CUST_1]]
- ← [[KS_STAGING.IRF_USER_DATA_CUST_2]]
- ← [[KS_STAGING.IRF_USER_DATA_KEYS]]
- ← [[KS_STAGING.USER_DATA_CUST_DIM_1]]
- ← [[KS_STAGING.USER_DATA_CUST_DIM_2]]
- ← [[KS_STAGING.USER_DATA_CUST_DIM_3]]
- ← [[KS_STAGING.USER_DATA_CUST_DIM_4]]
- ← [[KS_READER.DIM_USERS_RM]]
- ← [[KS_READER.DIM_TEAM_RM]]
- ← [[KS_READER.DIM_UNIT_RM]]
- ← [[KS_READER.DIM_SITE_RM]]
- ← [[KS_READER.DIM_COMPANY_RM]]
- ← [[KS_READER.DIM_USERCONTRACT_RM]]
- ← [[KS_READER.DIM_QUEUE_RM_V]]

