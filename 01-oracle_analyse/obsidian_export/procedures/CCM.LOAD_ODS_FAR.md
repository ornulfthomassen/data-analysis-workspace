# LOAD_ODS_FAR

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure implements a 'hot-swap' or 'blue-green deployment' strategy to refresh the `ODS_FAR` table with new data. It loads data from various source systems into a temporary table (`ODS_FAR_N`), creates necessary indexes, and then, under specific conditions (e.g., data volume change within a defined threshold), swaps `ODS_FAR_N` to become the new `ODS_FAR`. The old `ODS_FAR` is either renamed to a backup table (`ODS_FAR_O`) or dropped, ensuring high availability and a rollback mechanism. It also handles initial table creation and logs its execution status and any errors.

## Data Sources (Inputs)
- ← [[GALAXY.LOCATION_DIM]]
| Column Name |
|---|
| LOCATION_KEY |
| STREET_NAME |
| FLOOR_NUMBER |
| APPARTMENT_NUMBER |
| POSTCODE_ID |
| POST_OFFICE |
| HOUSE_NUMBER |
| HOUSE_CHARACTER |
| MUNICIPAL_ID |
| MUNICIPAL |
| COUNTY_ID |
| COUNTY |
| GRUNNKRETSNR |
| GRUNNKRETS |
| ADDRESS_ID |
| COORDINATE_X |
| COORDINATE_Y |
| LATITUDE |
| LONGITUDE |
| ADDRESS_TYPE_DESC |
| ADDRESS_STATUS_DESC |
| COUNTRY_NAME_2 |

- ← [[CCDW.GEOGRAPHY_ATTRIBUTES_FAR]]
| Column Name |
|---|
| GEOGRAPHY_ID |
| PROPERTY_PART_NUMBER |
| PROPERTY_ID |
| BRLID |
| GABADR_ADRNR |

- ← [[CCDW.COUNTRY]]
| Column Name |
|---|
| COUNTRY_NAME_2 |
| COUNTRY_ID |

- ← [[CCDW.ADDRESS_TYPE]]
| Column Name |
|---|
| ADDRESS_TYPE_DESC |
| ADDRESS_TYPE_ID |

- ← [[CCDW.ADDRESS_STATUS]]
| Column Name |
|---|
| ADDRESS_STATUS_DESC |
| ADDRESS_STATUS_ID |

- ← [[CCDW_CTI.CTI_CONS_HOUSEHOLD]]
| Column Name |
|---|
| FAR_ID |
| PLANNED_DECOM_DATE |

- ← [[KAS.BOLIG]]
| Column Name |
|---|
| FIBER_VIDERESOLGT_DATO |
| FIBER_VIDERESOLGT |
| ADRESSE_NR |

- ← [[KAS.ADRESSER]]
| Column Name |
|---|
| ADRESSE_NR |
| MATRIKKEL_ID |

- ← [[VULA.LOAD_VULA_WEB]]
| Column Name |
|---|
| created |
| state |
| type |
| FAR_ID |


## Target Tables (Outputs)
- → [[CCM.ODS_FAR]]
| Column Name |
|---|
| FARID |
| ADDRESS_TYPE |
| STREETNAME |
| FLOORNUMBER |
| FLATNUMBER |
| STREETPOSTALCODE |
| STREETPOSTALADDRESS |
| HOUSENUMBER |
| HOUSECHARACTER |
| TITLENUMBER |
| LANDNUMBER |
| MUNICIPALITY_CODE |
| MUNICIPALITY_NAME |
| COUNTY_CODE |
| COUNTY_NAME |
| CO_OPERATIVE_HOUSING_ID |
| BASIC_STATISTICAL_UNIT_ID |
| BASIC_STATISTICAL_UNIT_NAME |
| GAB_NUMBER |
| ADDRESS_STATUS |
| FLG_ADR_OK_BN |
| SUNRISE_SALE_END_DATE |
| SUNRISE_FIX_END_DATE |
| SUNRISE_TERMINATION_DATE |
| COORDINATE_X |
| COORDINATE_Y |
| LATITUDE |
| LONGITUDE |
| LUM_VULA_CHURN_DATE |
| LUM_VULA_CHURN_FLG |
| CDK_VULA_CHURN_DATE |
| CDK_VULA_CHURN_FLG |
| LOAD_DTTM |

- → [[CCM.ODS_FAR_N]]
| Column Name |
|---|
| FARID |
| ADDRESS_TYPE |
| STREETNAME |
| FLOORNUMBER |
| FLATNUMBER |
| STREETPOSTALCODE |
| STREETPOSTALADDRESS |
| HOUSENUMBER |
| HOUSECHARACTER |
| TITLENUMBER |
| LANDNUMBER |
| MUNICIPALITY_CODE |
| MUNICIPALITY_NAME |
| COUNTY_CODE |
| COUNTY_NAME |
| CO_OPERATIVE_HOUSING_ID |
| BASIC_STATISTICAL_UNIT_ID |
| BASIC_STATISTICAL_UNIT_NAME |
| GAB_NUMBER |
| ADDRESS_STATUS |
| FLG_ADR_OK_BN |
| SUNRISE_SALE_END_DATE |
| SUNRISE_FIX_END_DATE |
| SUNRISE_TERMINATION_DATE |
| COORDINATE_X |
| COORDINATE_Y |
| LATITUDE |
| LONGITUDE |
| LUM_VULA_CHURN_DATE |
| LUM_VULA_CHURN_FLG |
| CDK_VULA_CHURN_DATE |
| CDK_VULA_CHURN_FLG |
| LOAD_DTTM |

- → [[CCM.ODS_FAR_O]]
- → [[CCM.ODS_FAR_O_TEMP]]
- → [[CLM_CCM.ODS_PROCEDURE_SWAP_STATUS]]

