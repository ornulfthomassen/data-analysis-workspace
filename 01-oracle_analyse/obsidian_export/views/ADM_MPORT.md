# ADM_MPORT

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and enriches mobile number porting order data by linking it to subscription mapping information. It combines porting details (like order ID, arrival date, port date, service provider, order status) from `mport_port_report` with a corresponding `main_id_sk` from `adm_subscription_mapping`. The join is based on the phone number and ensures the order arrival date falls within the subscription's active period. For each porting order group, it selects the `main_id_sk` associated with the highest `main_number_rank` from the subscription mapping and formats the port date into a `yyyymm` period.

## Data Sources (Inputs)
- ← [[crm_analyse.mport_port_report]]
- ← [[crm_analyse.adm_subscription_mapping]]

