# P_ADM_ROLLOVER

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure `P_ADM_ROLLOVER` is designed to load and manage monthly 'rollover' data into a specific partition of the `CLM_ADM.ADM_ROLLOVER` table. It performs several steps:
1.  It checks for the existence of the target partitioned table `CLM_ADM.ADM_ROLLOVER` and the specific partition (`ADM_ROLLOVER_YYYYMM`) for the given month (`P_YYYYMM`).
2.  If the partition doesn't exist, it creates it using `ALTER TABLE ... ADD PARTITION`.
3.  It creates a temporary staging table, `CLM_ADM.TMP_ROLLOVER`, by selecting and transforming data from various source tables. The primary 'rollover' source table dynamically changes based on the month being processed (`P_FROM_TABLE` for newer data or `CLM_CCM.ROLLOVER` for older data).
4.  It then efficiently loads the data from the temporary table into the target partition using `ALTER TABLE ... EXCHANGE PARTITION ... WITH TABLE ...`.
5.  Finally, it computes statistics for the newly loaded partition to optimize query performance.
This procedure effectively provides a robust mechanism for monthly data ingestion into a large partitioned table, ensuring data integrity and allowing for controlled overwrites.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.ADM_MONTH_DIM]]
- ← [[CCDW.SUBSCRIPTION_MAPPING]]
- ← [[CM.SUBSCRIPTION_OFFER_INCENTIVE]]
- ← [[P_FROM_TABLE]]
- ← [[CLM_CCM.ROLLOVER]]

## Target Tables (Outputs)
- → [[CLM_ADM.ADM_ROLLOVER]]
- → [[CLM_ADM.TMP_ROLLOVER]]

