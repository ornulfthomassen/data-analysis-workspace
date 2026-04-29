# V_MAIN_NUMBER_2Y_PORT_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
This view summarizes the porting history for main numbers, providing an aggregated view of port-in and port-out events, associated service providers, and relevant dates over the last two years. It groups data by owner and main number to present a consolidated history for each unique main number within that period.

## Data Sources (Inputs)
- ← [[ADM_MOBIL_SUBSCR_HIST]]
| Column Name |
|---|
| OWNER |
| MAIN_NUMBER |
| CURRENT_STATUS |
| PORT_IN_DATE |
| PORT_IN_SERV_PROV_NAME |
| PORT_OUT_DATE |
| PORT_OUT_SERV_PROV_NAME |

