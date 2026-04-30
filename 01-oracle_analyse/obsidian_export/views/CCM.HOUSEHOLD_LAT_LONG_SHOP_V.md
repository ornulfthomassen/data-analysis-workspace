# HOUSEHOLD_LAT_LONG_SHOP_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view combines detailed household demographic and address information from 'CCM_HOUSEHOLD_INFO' with geographical coordinates (latitude, longitude) and distance metrics to shops from 'FARID_SHOP_DISTANCE'. It links these datasets using a 'FARID' identifier. The view includes logic to validate and potentially nullify invalid latitude and longitude values. Additionally, it appends two sets of placeholder rows using 'UNION ALL' for default or unknown household/shop distance scenarios.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]
| Column Name |
|---|
| HOUSEHOLD_ID |
| ANTALL_I_HUSSTAND |
| ADRESSE |
| POSTNR |
| POSTSTED |
| KOMMUNENR |
| GRUNNKRETS_NR |
| GRUNNKRETS |
| BOLIGTYPE |
| FARID |

- ← [[CCM.FARID_SHOP_DISTANCE]]
| Column Name |
|---|
| FARID |
| LATITUDE |
| LONGITUDE |
| TB_DISTANCE1 |
| TB_SOURCE_DEALER_ID1 |

- ← [[CCM.DUAL]]

