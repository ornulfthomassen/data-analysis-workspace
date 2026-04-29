# VYA_TM_PAD_ORDERS

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed for loading 'PAD Orders' data into a system referred to as 'Mjøsa'. It joins order details with customer mapping information to enrich order records with customer and main order customer keys.

## Data Sources (Inputs)
- ← [[PAD_STAGE.PAD_ORDERS]]
| Column Name |
|---|
| ORDERTYPE |
| ORDERID |
| CALLDATE |
| CONSULT |
| WHYREASON |
| WRSTCD |
| WHYREASONDESCRIPTION |
| CELLPACKAGESK |
| RESPTRACINGCODE |
| COSORDERID |
| COSTTRANSFERDATE |
| TIMEOFCONTACT |
| MAINPRODUCTID |
| MAINPRODUCTDESC |
| NOOFCALLBACKS |
| CONCENTREQUESTED |
| CONCENTRECEIVED |
| BACKTOCALLLIST |
| ANSWERINGMACHINE |
| BUSINESSAREAID |
| DEALERID |
| DEALERIDDESC |
| CAMPAIGN_CD |
| CAMPAIGN_NM |
| HOUSEHOLD_ID |
| LOAD_DTTM |
| KURTID |
| MAINORDERKURT |
- ← [[CRM_ANALYSE.ADM_CUSTOMER_MAPPING_V]]
| Column Name |
|---|
| CUSTOMER_KEY |
| KURT_ID |

