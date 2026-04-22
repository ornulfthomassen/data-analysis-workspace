# P_ADM_SUBSCR_HANDSET_HIST_AGG

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure aggregates historical subscription handset usage data. It identifies the first and last recorded periods of use, terminal dates, and various device attributes (like producer name, model name, OS type, category, etc.) for each unique subscription and model ID. The procedure's primary action is to drop and then recreate the `ADM_SUBSCR_HANDSET_HIST_AGG` table, completely replacing its contents with the newly aggregated data. It includes checks to ensure source data availability and logs its operational status and any errors.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_SUBSCR_HANDSET_HIST]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST_AGG]]

