# P_CU_ODS_CUST_CONTACT_ADDRESS

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure refreshes the ODS_CUST_CONTACT_ADDRESS table with updated and prioritized customer contact address data. It performs a full load by creating a new temporary table (`ODS_CUST_CONTACT_ADDRESS_N`), populating it with processed data from various source systems, applying data quality rules and ranking logic. It then compares the row count of the new data with the existing target table. If the row count difference is within an acceptable threshold (or forced), it renames the current ODS_CUST_CONTACT_ADDRESS to ODS_CUST_CONTACT_ADDRESS_O (as a backup) and renames the new temporary table (ODS_CUST_CONTACT_ADDRESS_N) to ODS_CUST_CONTACT_ADDRESS. The procedure also manages indexes and grants permissions on the newly established target table.

## Data Sources (Inputs)
- ← [[CCM.ODS_CUST_CONTACT_ADDRESS]]
- ← [[CDC.MASTER_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| MASTER_ID |
| INFO_IS_DELETED |
| CUST_STATUS_ID |
| UNIT_TYPE_ID |

- ← [[CDC.ADDRESS_LINK]]
| Column Name |
|---|
| MASTER_ID |
| INFO_IS_DELETED |
| VALID_TO_DATE |
| ADDRESS_LOCATION_ID |
| VALID_FROM_DATE |
| ADDRESS_TYPE_LINK_ID |

- ← [[CDC.ADDRESS]]
| Column Name |
|---|
| ADDRESS_TYPE_LINK_ID |
| INFO_IS_DELETED |
| FAR_ID |
| ADDRESS_FORMAT_TYPE_ID |
| ADDRESS_STREET |
| POSTCODE_NAME |
| POSTCODE_ID |
| STREET_NAME |
| HOUSE_NUMBER |
| HOUSE_CHARACTER |
| CO_ADDRESS_NAME |
| ADDRESS_LINE_1 |
| POSTBOX_ADDRESS_NAME |
| POSTAL_AREA_NAME |
| ADDRESS_LINE_2 |
| ADDRESS_LINE_3 |
| COUNTRY_CODE |

- ← [[CDC.ADDRESS_LOCATION]]
| Column Name |
|---|
| ADDRESS_LOCATION_ID |
| ADDRESS_LOCATION_NAME |

- ← [[CCDW.COUNTRY]]
| Column Name |
|---|
| COUNTRY_NAME_2 |
| COUNTRY_NAME_FULL |

- ← [[ODS.CUSTOMER_ODS]]
| Column Name |
|---|
| CUSTOMER_ID |
| OWNER_MOB_SUB_NUM |
| OWNER_MOB_AGR_NUM |
| ORGANISATION_NUMBER |

- ← [[CRM_ANALYSE.COUNTRY_DIM]]
| Column Name |
|---|
| ISO3166_1_ALPHA_2 |
| SHORT_NAME_EN |


## Target Tables (Outputs)
- → [[CCM.ODS_CUST_CONTACT_ADDRESS_N]]
| Column Name |
|---|
| KURT_ID |
| FAR_ID |
| CONTACT_ADR_LINK_DTTM |
| CONTACT_ADR_LOCATION_ID |
| CONTACT_ADR_LOCATION_NAME |
| CONTACT_ADR_FORMAT_TYPE_ID |
| CONTACT_ADR_QUALITY |
| CONTACT_ADR_LINE_1 |
| CONTACT_ADR_LINE_2 |
| CONTACT_ADR_LINE_3 |
| CONTACT_ADR_COUNTRY_NAME |
| POSTCODE_ID |
| POSTCODE_NAME |
| CONTACT_ADR_RANK |
| CONTACT_ADR_SRC |
| LOAD_DTTM |

- → [[CCM.ODS_CUST_CONTACT_ADDRESS_O]]
- → [[CCM.ODS_CUST_CONTACT_ADDRESS]]
| Column Name |
|---|
| KURT_ID |
| FAR_ID |
| CONTACT_ADR_LINK_DTTM |
| CONTACT_ADR_LOCATION_ID |
| CONTACT_ADR_LOCATION_NAME |
| CONTACT_ADR_FORMAT_TYPE_ID |
| CONTACT_ADR_QUALITY |
| CONTACT_ADR_LINE_1 |
| CONTACT_ADR_LINE_2 |
| CONTACT_ADR_LINE_3 |
| CONTACT_ADR_COUNTRY_NAME |
| POSTCODE_ID |
| POSTCODE_NAME |
| CONTACT_ADR_RANK |
| CONTACT_ADR_SRC |
| LOAD_DTTM |


