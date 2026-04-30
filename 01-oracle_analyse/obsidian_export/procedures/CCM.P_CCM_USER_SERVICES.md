# P_CCM_USER_SERVICES

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure consolidates and summarizes user service information, specifically for users with Norwegian phone numbers. It first identifies user IDs associated with Norwegian phone numbers from two different phone service tables, storing them in a temporary helper table. Then, it aggregates service usage data (first access, last access, and last used times) for these identified users from a service history table, joining with the helper table and a daily activity log, and stores the results in another helper table. Finally, it creates a unique index on the aggregated service usage table.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_PHONES]]
| Column Name |
|---|
| user_id |
| file_date |
| PHONES |

- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| user_id |
| PH_MSISDN |

- ← [[COMOYO.MINSKY_MAIN_DAILY]]
| Column Name |
|---|
| load_date |
| GLOBAL_ID |
| LAST_CONNECTION_DTTM |

- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
| Column Name |
|---|
| USER_ID |
| SERVICE_NAME |
| SERVICE_FIRST_DATE |
| END_DATE |
| current_record |

- ← [[CCM.CCM_USER_SERVICE_NO_TMP]]
| Column Name |
|---|
| user_id |


## Target Tables (Outputs)
- → [[CCM.CCM_USER_SERVICE_NO_TMP]]
| Column Name |
|---|
| user_id |

- → [[CCM.CCM_USER_SERVICES_CP]]
| Column Name |
|---|
| USER_ID |
| SERVICE_CD |
| FIRST_ACCESS_TM |
| LAST_ACCESS_TM |
| LAST_USED |


