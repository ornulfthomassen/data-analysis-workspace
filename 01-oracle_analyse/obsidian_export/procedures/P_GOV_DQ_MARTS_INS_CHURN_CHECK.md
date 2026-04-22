# P_GOV_DQ_MARTS_INS_CHURN_CHECK

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure performs data quality checks on weekly mobile segment churn data. It calculates and compares various churn and subscriber metrics (total, by brand - Telenor/djuice, and by profit category - 'Topp 35'/'Bunn 65') between the current week and the previous week. It identifies significant percentage-point or absolute changes in these metrics and also verifies the existence of data partitions for the processed weeks. The results of these data quality checks, including an 'OK' status or specific error reasons for detected anomalies or missing data, are recorded into a data quality monitoring table.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.BALANCE_MOBILE_SEGMENT_W_AGG]]
- ← [[GALAXY.DATE_DIM_MV]]
- ← [[SYS.ALL_OBJECTS]]
- ← [[DUAL]]

## Target Tables (Outputs)
- → [[CCM.GOV_DQ_MARTS]]

