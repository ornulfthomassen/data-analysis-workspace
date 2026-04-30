# P_HH_ODS_HOUSEHOLD_CORE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure calculates and aggregates various household core features, such as demographics, building types, and broadband product group information. It creates a new temporary table (`ODS_HOUSEHOLD_CORE_N`) with this data, then performs a table swap (rename) to replace the existing permanent `ODS_HOUSEHOLD_CORE` table. The old `ODS_HOUSEHOLD_CORE` table is kept as a backup (`ODS_HOUSEHOLD_CORE_O`). The procedure also manages index creation/renaming and grants privileges on the newly updated table, and gathers table statistics.

## Data Sources (Inputs)
- ← [[CLM_CCM.ODS_HOUSEHOLD_CORE]]
- ← [[CLM_CCM.ODS_SUBSCRIPTION_MV]]
| Column Name |
|---|
| FAR_ID_INSTALL |
| PRODUCT_OFFER_ID |
| BUSINESS_AREA_ID |

- ← [[CLM_CCM.ODS_PRODUCT_DIM]]
| Column Name |
|---|
| PRODUCT_KEY |
| PRODUCT_GROUP |
| PRODUCT_DESC |
| SOURCE_SYSTEM_NAME |
| PRIMARY_PRODUCT_FLAG |
| POID |

- ← [[FAR.FARADR]]
| Column Name |
|---|
| GABADR_ADRNR |
| ADRIDENT |

- ← [[CCDW.HOUSEHOLD]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| GEOGRAPHY_ID |
| GABADR_ADRNR |
| BYGNINGSTYPE_NR |
| HOUSEHOLD_MEMBER_QUANTITY |
| ADULTS_HOUSEHOLD_QUANTITY |
| CHILDREN_HOUSEHOLD_QUANTITY |

- ← [[FAR.ADDRESS_PROPERTIES]]
| Column Name |
|---|
| FARID |
| CURRENT_STATUS |
| BOLIGTYPE |
| ANTALLBOENHETER |
| ANTALLBEDRIFTER |
| SQMETER |
| BYGNINGSTYPE_NR |

- ← [[CRM_ANALYSE.ADM_BUILDING_TYPE_DIM]]
| Column Name |
|---|
| BUILDING_CODE_LEVEL3 |
| RESIDENCE_TYPE |

- ← [[CCM.ALL_INDEXES]]
| Column Name |
|---|
| OWNER |
| TABLE_NAME |
| INDEX_NAME |


## Target Tables (Outputs)
- → [[CLM_CCM.ODS_HOUSEHOLD_CORE_N]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FAR_ID |
| GAB_NUMBER |
| BYGNINGSTYPE_NR |
| BOLIGTYPE |
| BOLIGTYPE_SSB |
| NBR_BOENHETER |
| NBR_BEDRIFTER |
| SQUARE_METER |
| HOUSEHOLD_MEMBER_COUNT |
| NBR_MEMBERS_ADULT |
| NBR_MEMBERS_U18 |
| BB_PRODUCT_GROUP_HH_ADR |
| BB_PRODUCT_GROUP_HH_GAB |
| PRODUCT_KOLLEKTIV_FLG_GAB |

- → [[CLM_CCM.ODS_HOUSEHOLD_CORE]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| FAR_ID |
| GAB_NUMBER |
| BYGNINGSTYPE_NR |
| BOLIGTYPE |
| BOLIGTYPE_SSB |
| NBR_BOENHETER |
| NBR_BEDRIFTER |
| SQUARE_METER |
| HOUSEHOLD_MEMBER_COUNT |
| NBR_MEMBERS_ADULT |
| NBR_MEMBERS_U18 |
| BB_PRODUCT_GROUP_HH_ADR |
| BB_PRODUCT_GROUP_HH_GAB |
| PRODUCT_KOLLEKTIV_FLG_GAB |

- → [[CLM_CCM.ODS_HOUSEHOLD_CORE_O]]

