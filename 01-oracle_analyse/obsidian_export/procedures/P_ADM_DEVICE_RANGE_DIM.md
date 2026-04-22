# P_ADM_DEVICE_RANGE_DIM

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The Oracle SQL procedure `P_ADM_DEVICE_RANGE_DIM` is designed to build and maintain a device dimension table, `ADM_DEVICE_RANGE_DIM`. Its primary purpose is to categorize and enrich device information by performing the following steps:
1.  **Identifies and Inserts New Devices**: It identifies new device types from subscription, handset, and GSMA marketing name data that are not yet present in `ADM_DEVICE_RANGE_DIM` and inserts them. During insertion, it assigns an initial `DEVICE_RANGE` (e.g., 'High-End', 'Mid-Range', 'Low-End', 'Rugged', 'Senior', 'Annet') based on patterns found in marketing names and manufacturers.
2.  **Counts Active Terminals**: It creates a temporary intermediate table (`CURRENT_TERMINAL_USE`) to count the number of currently active terminals for each `TAC_ID` based on live subscription and handset data.
3.  **Updates Max Terminal Count**: It updates the `MAX_NO_TERMINALS` column in `ADM_DEVICE_RANGE_DIM` for existing devices, taking the greatest value between the current `MAX_NO_TERMINALS` and the newly calculated active terminal count from `CURRENT_TERMINAL_USE`.
4.  **Standardizes Model Information**: It updates `MODEL_ID` and `MODEL_MARKETING_NAME` in `ADM_DEVICE_RANGE_DIM` by synchronizing with `ADM_GSMA_MARKETING_NAME_DIM` where data differs.
5.  **Aggregates Marketing Names**: It calculates and updates `NAVNEVARIANTER` (number of marketing name variants), `MAIN_MODEL_MARKETING_NAME` (the most prevalent marketing name based on terminal count), and `LIST_MARKETING_NAME_L1` (a concatenated list of marketing name variants) within `ADM_DEVICE_RANGE_DIM` itself.
6.  **Determines Main Device Range**: It determines and updates the `MAIN_DEVICE_RANGE` for each model in `ADM_DEVICE_RANGE_DIM` based on the most common `DEVICE_RANGE` among its entries, prioritized by the total number of terminals.
7.  **Error Handling**: The procedure includes extensive error handling mechanisms, logging any issues to `CRM_ANALYSE.P_ADM_LOAD_HISTORY` for monitoring and debugging.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[CCDW.SUBSCRIPTION_HANDSET]]
- ← [[CCDW.HANDSET_TYPE_EXT]]
- ← [[ADM_GSMA_MARKETING_NAME_DIM]]
- ← [[ADM_DEVICE_RANGE_DIM]]
- ← [[CURRENT_TERMINAL_USE]]

## Target Tables (Outputs)
- → [[ADM_DEVICE_RANGE_DIM]]
- → [[CURRENT_TERMINAL_USE]]

