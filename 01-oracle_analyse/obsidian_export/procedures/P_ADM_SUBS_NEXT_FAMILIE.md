# P_ADM_SUBS_NEXT_FAMILIE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure processes subscription product data for a given month (P_YYYYMM). It first extracts detailed subscription records from the `CCDW.SUBSCRIBED_PRODUCT` table into a temporary table (`TMP_SUBS_NEXT_FAMILIE_DET`). This detailed temporary data is then integrated into a monthly partition of a permanent, partitioned detail table (`ADM_SUBS_NEXT_FAMILIE_DET`) using an `ALTER TABLE ... EXCHANGE PARTITION` operation. Subsequently, the procedure aggregates data from the `ADM_SUBS_NEXT_FAMILIE_DET` table, calculating last subscription details and rankings, and stores these aggregated results in another temporary table (`TMP_SUBS_NEXT_FAMILIE_AGG`). Finally, this aggregated temporary data is also integrated into a monthly partition of a permanent, partitioned aggregated table (`ADM_SUBS_NEXT_FAMILIE_AGG`) via an `EXCHANGE PARTITION`. The procedure includes checks for source data existence and handles table/partition creation and error logging.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIBED_PRODUCT]]
- ← [[CLM_ADM.ADM_SUBSCRIPTION_HISTORY]]
- ← [[ADM_SUBS_NEXT_FAMILIE_DET]]

## Target Tables (Outputs)
- → [[TMP_SUBS_NEXT_FAMILIE_DET]]
- → [[ADM_SUBS_NEXT_FAMILIE_DET]]
- → [[TMP_SUBS_NEXT_FAMILIE_AGG]]
- → [[ADM_SUBS_NEXT_FAMILIE_AGG]]

