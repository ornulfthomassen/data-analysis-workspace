# V_OWNER_2Y_PORT_HIST

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates porting history data for owners, providing statistics such as the count of port-ins and port-outs, distinct main numbers, and active statuses. It also calculates the minimum and maximum dates for port-in and port-out events and lists the service providers involved in these events, specifically focusing on data from the last two years.

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

