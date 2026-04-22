# KS_INTERACTION_V_OLD

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KS_INTERACTION_V_OLD`, provides a comprehensive, denormalized record of customer interactions (likely calls or other media) within a contact center or customer service environment. It combines core interaction facts with details about involved resources (agents, queues), interaction types, media types, various duration metrics (total, queue, handle, wrap, hold), technical outcomes, and extensive custom user-defined data. It also enriches the interaction data with organizational hierarchy information (employee, team, unit, site, company) and performs data type conversions for dates and phone numbers, making it suitable for reporting and analytical purposes. The join to `KS_INTERACTION_LOAD_LOG_V` suggests it may be used in an incremental data loading process.

## Data Sources (Inputs)
- ← [[KS_STAGING.INTERACTION_FACT]]
- ← [[CRM_ANALYSE.KS_INTERACTION_LOAD_LOG_V]]
- ← [[KS_STAGING.INTERACTION_RESOURCE_FACT]]
- ← [[KS_STAGING.MEDIATION_SEGMENT_FACT]]
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

