# P_HH_ODS_HOUSEHOLD_DEMOGRAPHY

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Calculates and aggregates demographic information for households and their adult and child members, including age generations, age categories, and couple indicators. It then updates the `ODS_HOUSEHOLD_DEMOGRAPHY` table using a table swap mechanism, creating a new version of the table (`ODS_HOUSEHOLD_DEMOGRAPHY_N`), populating it, and then renaming it to become the active production table. The previous version of the table is backed up (`ODS_HOUSEHOLD_DEMOGRAPHY_O`). It also handles index recreation and renaming during the swap, gathers table statistics, and logs execution status or errors to a history table.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_HOUSEHOLD_DEMOGRAPHY]]
- ← [[CCDW.HOUSEHOLD_MEMBER]]
| Column Name |
|---|
| CUSTOMER_ID |
| HOUSEHOLD_ID |

- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| CUSTOMER_STATUS_ID |
| CUSTOMER_TYPE_ID |
| CUSTOMER_AGE |
| HOUSEHOLD_ID |

- ← [[CLM_CCM.ODS_CUSTOMER_PROF]]
| Column Name |
|---|
| KURT_ID |
| GENDER |

- ← [[CCDW.HOUSEHOLD]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| GEOGRAPHY_ID |
| GABADR_ADRNR |

- ← [[CLM_CCM.WORK_HH_GEN_INPUT]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| AGE_GEN |
| KURT_ID |
| AGE |
| HH_GEN_SEC_CATEGORY |
| GENDER |

- ← [[CLM_CCM.ODS_CUSTOMER]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| CUSTOMER_AGE |
| CUSTOMER_STATUS_ID |
| CUSTOMER_TYPE_ID |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |


## Target Tables (Outputs)
- → [[CLM_CCM.WORK_HH_GEN_INPUT]]
| Column Name |
|---|
| KURT_ID |
| HOUSEHOLD_ID |
| GENDER |
| AGE |
| AGE_PREV_HH_MEMBER |
| AGE_DIFF_PREV_HH_MEMBER |
| HH_AGE_GEN |
| ADD_AGE_GEN |
| AGE_GEN |
| ANTALL_GEN |
| HH_GEN_SEC_CATEGORY |

- → [[CLM_CCM.ODS_HOUSEHOLD_DEMOGRAPHY_N]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FAR_ID |
| GAB_NUMBER |
| NBR_HH_AGE_GEN |
| NBR_HH_MEMB_ADULT |
| AGE_MIN_HH_ADULT |
| AGE_MAX_HH_ADULT |
| NBR_HH_MEMB_CHILDREN |
| AGE_MIN_HH_CHILD |
| AGE_MAX_HH_CHILD |
| NBR_HH_MEMB_CHILDREN_0_5YRS |
| NBR_HH_MEMB_CHILDREN_6_12YRS |
| NBR_HH_MEMB_CHILDREN_13_17YRS |
| SEC_HH_GEN_CATEGORY |
| COUPLE_FLG |

- → [[CLM_CCM.ODS_HOUSEHOLD_DEMOGRAPHY_O]]
- → [[CLM_CCM.ODS_HOUSEHOLD_DEMOGRAPHY]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FAR_ID |
| GAB_NUMBER |
| NBR_HH_AGE_GEN |
| NBR_HH_MEMB_ADULT |
| AGE_MIN_HH_ADULT |
| AGE_MAX_HH_ADULT |
| NBR_HH_MEMB_CHILDREN |
| AGE_MIN_HH_CHILD |
| AGE_MAX_HH_CHILD |
| NBR_HH_MEMB_CHILDREN_0_5YRS |
| NBR_HH_MEMB_CHILDREN_6_12YRS |
| NBR_HH_MEMB_CHILDREN_13_17YRS |
| SEC_HH_GEN_CATEGORY |
| COUPLE_FLG |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| TABLE_NAME |
| START_DTTM |
| STATUS |
| STATUS_MESSAGE |
| WORKFLOW_NAME |
| SESSION_NAME |


