# ZUPDATE_MAIN_PRODUCT_START_DATE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure updates the main product start date and associated product identifiers for subscriptions in the `CCM_SUBSCRIPTION` table where the `MAIN_PRODUCT_START_DATE` is currently null. It identifies new main product details by joining `CCM_SUBSCRIPTION` with `CCM_SUBSCR_SERVICES_INFO`, `CM.SUBSCRIPTION_OFFER_INCENTIVE`, and `CLM_CCM.CCM_PRODUCT_TYPE_CONFIG`. The procedure then updates `MAIN_PRODUCT_ID`, `MAIN_PRODUCT_START_DATE`, `MAIN_PRODUCT_END_DATE`, and `LOAD_DTTM` in `CCM_SUBSCRIPTION`, and `PRODUCT_OFFER_ID_MARKET`, `PRODUCT_OFFER_SOURCE_ID_MARKET`, `PRODUCT_OFFER_ID_MARKET_PREV`, `START_DATE_MARKET_PRODUCT`, and `PRODUCT_OFFER_MARKET_CHG_FLG` in `CCM_SUBSCR_SERVICES_INFO`. It logs the execution timestamp and the count of updated records into a dynamically created tracking table named `LOG_SUBSCR_MAIN_PROD_START_DT`. The entire operation is executed only when the database name is 'CCDWP'.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
| Column Name |
|---|
| OBJECT_TYPE |
| OBJECT_NAME |
| OWNER |

- ← [[CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| MAIN_NUMBER |
| MAIN_PRODUCT_ID |
| MAIN_PRODUCT_START_DATE |
| SOURCE_SYSTEM_SUBSCR_ID_1 |

- ← [[CCM.CCM_SUBSCR_SERVICES_INFO]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| PRODUCT_OFFER_SOURCE_ID_MARKET |

- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
| Column Name |
|---|
| SUBSCR_ID |
| INFO_IS_DELETED |
| INC_VALID_TO_DATE |
| INC_VALID_FROM_DATE |
| PRODUCT_OFFER_ID |

- ← [[CLM_CCM.CCM_PRODUCT_TYPE_CONFIG]]
| Column Name |
|---|
| ID |
| PARENT |
| VALUE |


## Target Tables (Outputs)
- → [[CCM.LOG_SUBSCR_MAIN_PROD_START_DT]]
| Column Name |
|---|
| UPDATE_DTTM |
| ANTALL_OPPDATERT |

- → [[CCM.CCM_SUBSCRIPTION]]
| Column Name |
|---|
| MAIN_PRODUCT_ID |
| MAIN_PRODUCT_START_DATE |
| MAIN_PRODUCT_END_DATE |
| LOAD_DTTM |

- → [[CCM.CCM_SUBSCR_SERVICES_INFO]]
| Column Name |
|---|
| PRODUCT_OFFER_ID_MARKET |
| PRODUCT_OFFER_SOURCE_ID_MARKET |
| PRODUCT_OFFER_ID_MARKET_PREV |
| START_DATE_MARKET_PRODUCT |
| PRODUCT_OFFER_MARKET_CHG_FLG |


