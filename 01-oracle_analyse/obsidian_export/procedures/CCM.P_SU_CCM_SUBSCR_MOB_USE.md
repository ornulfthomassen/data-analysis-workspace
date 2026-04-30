# P_SU_CCM_SUBSCR_MOB_USE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure calculates mobile subscription usage, rollover, and profit metrics at the subscription level. It populates a new temporary table (`CLM_CCM.CCM_SUBSCR_MOB_USE_N`) with these derived features. After performing a row count validation against the existing target table (`CLM_CCM.CCM_SUBSCR_MOB_USE`), it executes a table swap operation. The existing target table is renamed to a backup table (`CLM_CCM.CCM_SUBSCR_MOB_USE_O`), and the newly created temporary table is renamed to become the new permanent target table (`CLM_CCM.CCM_SUBSCR_MOB_USE`). The procedure also handles dynamic index creation on the temporary table, index renaming during the swap, and grants appropriate permissions. Errors and warnings are logged to the `CLM_CCM.CCM_LOAD_HISTORY` table.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_SUBSCR_MOB_USE]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| SUBSCR_START_DATE |
| PRODUCT_OFFER_START_DATE |
| PRODUCT_OFFER_END_DATE |
| PRODUCT_OFFER_ID |
| BUSINESS_AREA_ID |
| MARKET_AREA_ID |

- ← [[CLM_CCM.ODS_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| SOURCE_SYSTEM_NAME |
| INCLUDED_MB |

- ← [[CLM_CCM.CCM_SUBSCR_MOB_USAGE_MONTH_V]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAX_PERIOD_MONTH_KEY_USE |
| MB_HOME_NORMAL_LAST1 |
| MB_HOME_NORMAL_LAST2 |
| MB_HOME_NORMAL_LAST3 |

- ← [[CRM_ANALYSE.ADM_MONTH_DIM_V]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| RELATIVE_MONTH |

- ← [[CLM_CCM.ROLLOVER]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_MONTH_KEY |
| SUM_BALANCE_MB |

- ← [[CLM_ADM.ADM_PROFIT_CAT_MND_SUBS_HIST]]
| Column Name |
|---|
| PERIOD_MONTH_KEY |
| SUBSCRIPTION_ID |
| NET_AMOUNT_USE |
| NET_DISCOUNT_AMOUNT_USE |
| NET_INITIATION_FEE |
| NET_DISCOUNT_STARTUP_FEE |
| NET_PERIODIC_FEE |
| NET_DISCOUNT_FIXED_FEE |

- ← [[CCDW_USAGE.SUBSCR_PREPAID_INACTIVE_AGG]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PERIOD_ID |
| LAST_TRAFFIC_EVENT_DATE |
| LAST_EVENT_DATE |
| BUSINESS_AREA_ID |
| SOURCE_SYSTEM_ID |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |


## Target Tables (Outputs)
- → [[CLM_CCM.CCM_SUBSCR_MOB_USE_N]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| USE_SUBSCR_ACTIVE_3MO_FLG |
| USE_SUBSCR_LAST_ACTIVE_DTTM |
| NET_REV_MAX_MONTH_KEY |
| NET_REV_USE_LAST1 |
| NET_REV_FEE_LAST1 |
| PCT_USED_INCL_MB_PROD_AVG_3MO |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| PCT_P_USE_LAST1_BY_CUR_F_UNIT |

- → [[CLM_CCM.CCM_SUBSCR_MOB_USE_O]]
- → [[CLM_CCM.CCM_SUBSCR_MOB_USE]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| USE_SUBSCR_ACTIVE_3MO_FLG |
| USE_SUBSCR_LAST_ACTIVE_DTTM |
| NET_REV_MAX_MONTH_KEY |
| NET_REV_USE_LAST1 |
| NET_REV_FEE_LAST1 |
| PCT_USED_INCL_MB_PROD_AVG_3MO |
| PCT_USED_INCL_MB_PROD_AVG_1MO |
| PCT_P_USE_LAST1_BY_CUR_F_UNIT |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]
| Column Name |
|---|
| OBJECT_NAME |
| START_DTTM |
| STATUS |
| STATUS_MESSAGE |
| WORKFLOW_NAME |
| SESSION_NAME |


