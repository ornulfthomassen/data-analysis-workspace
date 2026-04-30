# P_EV_ODS_TALKMORE_EVENTS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure processes Talkmore event data to generate an aggregated and enriched dataset, `ODS_TALKMORE_EVENTS`, for telemarketing list production. It employs a table-swap strategy: it first builds a new version of the table (`ODS_TALKMORE_EVENTS_N`) by joining and transforming data from multiple source tables, then conditionally renames the existing `ODS_TALKMORE_EVENTS` to a backup (`ODS_TALKMORE_EVENTS_O`), and finally renames the newly built table (`ODS_TALKMORE_EVENTS_N`) to `ODS_TALKMORE_EVENTS`. The swap is conditional on the row count difference between the new and old datasets falling within a predefined threshold. It also handles index creation/renaming and logging of the process status.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_TALKMORE_EVENTS]]
- ← [[TALKMORE.TALKMORE_EVENT_WINBACK]]
| Column Name |
|---|
| RESOURCE_VALUE |
| EVENT_LOAD_DTTM |
| EVENT_TYPE |
| CUSTOMER_ID |
| SRC_SEQ_ID |
| CONTRACT_ID |
| RESOURCE_VALUE_DESC |
| EVENT_DTTM |
| EVENT_END_DTTM |
| FIRST_NAME |
| LAST_NAME |
| STREET_ADDRESS |
| POSTAL_CODE |
| POSTAL_ADDRESS |
| BIRTH_DATE |
| CONTRACT_PHONE_NUMBER |
| CONTRACT_EMAIL_ADDRESS |
| EXTRA_INFO_1 |
| EXTRA_INFO_2 |
| EXTRA_INFO_3 |

- ← [[NRPORT.NRPORT_PORTERINGER]]
| Column Name |
|---|
| MSISDN_ID |
| SERVICE_PROVIDER_ID_PORT_FROM |
| PORT_LOG_VALID_FROM_DATE |

- ← [[NRPORT.NRPORT_SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER_ID |
| SERVICE_PROVIDER_NAME |

- ← [[ONL_REP.SERVICE_ORDER]]
| Column Name |
|---|
| ORDER_ID |
| ORDER_STATUS_ID |
| ORDER_ORIGINATOR_ID |
| ORDER_PROCESSED_DATE |

- ← [[ONL_REP.SERVICE_ORDER_PRODUCT]]
| Column Name |
|---|
| ORDER_ID |
| PRODUCT_ACTION_TYPE_ID |
| PRODUCT_STATUS_ID |
| ORDER_PHONE_NUM |

- ← [[ONL_REP.SERVICE_ORDER_PRODUCT_PARAM]]
| Column Name |
|---|
| ORDER_ID |
| PARAM_ID |
| PARAM_VALUE |

- ← [[TALKMORE.TALKMORE_EVENTS_MATCH]]
| Column Name |
|---|
| CUSTOMER_KEY |
| MATCH_DESC |
| CUSTOMER_ID |

- ← [[CLM_CCM.ODS_MSISDN_SERVICE_PROVIDER]]
| Column Name |
|---|
| SERVICE_PROVIDER |
| MAIN_NUMBER |
| R_NUM |
| CURRENT_STATUS |
| SERVICE_TYPE |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |


## Target Tables (Outputs)
- → [[CLM_CCM.ODS_TALKMORE_EVENTS_N]]
| Column Name |
|---|
| KURT_ID |
| MATCH_DESC |
| SRC_SEQ_ID |
| SRC_CUSTOMER_ID |
| SRC_CONTRACT_ID |
| RESOURCE_VALUE |
| RESOURCE_VALUE_DESC |
| EVENT_TYPE |
| EVENT_DTTM |
| EVENT_LOAD_DTTM |
| EVENT_END_DTTM |
| FIRST_NAME |
| LAST_NAME |
| STREET_ADDRESS |
| POSTAL_CODE |
| POSTAL_ADDRESS |
| BIRTH_DATE |
| CONTACT_PHONE_NUMER |
| CONTACT_EMAIL_ADDRESS |
| EXTRA_INFO_1 |
| EXTRA_INFO_2 |
| EXTRA_INFO_3 |
| SERVICE_PROVIDER_CURRENT |
| NBR_PORT_ORDERS_2YRS |
| NRDB_NBR_PORT_ORDERS_2YRS |
| NRDB_MAX_PORT_DT |
| INBOUND_PORTORDER |

- → [[CLM_CCM.ODS_TALKMORE_EVENTS_O]]
- → [[CLM_CCM.ODS_TALKMORE_EVENTS]]
| Column Name |
|---|
| KURT_ID |
| MATCH_DESC |
| SRC_SEQ_ID |
| SRC_CUSTOMER_ID |
| SRC_CONTRACT_ID |
| RESOURCE_VALUE |
| RESOURCE_VALUE_DESC |
| EVENT_TYPE |
| EVENT_DTTM |
| EVENT_LOAD_DTTM |
| EVENT_END_DTTM |
| FIRST_NAME |
| LAST_NAME |
| STREET_ADDRESS |
| POSTAL_CODE |
| POSTAL_ADDRESS |
| BIRTH_DATE |
| CONTACT_PHONE_NUMER |
| CONTACT_EMAIL_ADDRESS |
| EXTRA_INFO_1 |
| EXTRA_INFO_2 |
| EXTRA_INFO_3 |
| SERVICE_PROVIDER_CURRENT |
| NBR_PORT_ORDERS_2YRS |
| NRDB_NBR_PORT_ORDERS_2YRS |
| NRDB_MAX_PORT_DT |
| INBOUND_PORTORDER |

- → [[CLM_CCM.CCM_LOAD_HISTORY]]

