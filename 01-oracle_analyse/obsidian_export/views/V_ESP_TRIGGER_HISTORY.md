# V_ESP_TRIGGER_HISTORY

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a projection of historical ESP trigger data, selecting most columns directly from the source table while explicitly setting a few specific columns (inputs_espkurtid, sourcecustomerid, inputs_espmainnumber) to NULL. It serves as a simplified interface or a specific subset of the underlying trigger history.

## Data Sources (Inputs)
- ← [[clm_rtdm.esp_trigger_history]]

