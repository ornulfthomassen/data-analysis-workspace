# CUSTOMER_RES_AND_APP_V

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of customer SMS reservation and acceptance details. It translates raw SMS indicator values into distinct binary flags for reservation and acceptance, and links customer identifiers from an operational data store to a master customer key from a mapping table. The view focuses on records where the SMS indicator denotes an active reservation or acceptance.

## Data Sources (Inputs)
- ← [[ODS.ANA_CUSTOMER_RES_AND_APP]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

