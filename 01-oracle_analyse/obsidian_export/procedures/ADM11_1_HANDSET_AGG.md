# ADM11_1_HANDSET_AGG

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The procedure aggregates historical handset data. It operates in two main stages: first, it processes raw subscription-level handset history data from 'ADM_SUBSCR_HANDSET_HIST' to create an aggregated view called 'ADM_SUBSCR_HANDSET_HIST_AGG'. Then, it further aggregates this subscription-level aggregated data ('ADM_SUBSCR_HANDSET_HIST_AGG') to generate a model-level summary in 'ADM_HANDSET_HIST_AGG'. Both target tables are dropped (if they exist) and then recreated completely with fresh aggregated data upon each execution, ensuring the data is always up-to-date.

## Data Sources (Inputs)
- ← [[SYS.ALL_OBJECTS]]
- ← [[ADM_SUBSCR_HANDSET_HIST]]
- ← [[ADM_SUBSCR_HANDSET_HIST_AGG]]

## Target Tables (Outputs)
- → [[ADM_SUBSCR_HANDSET_HIST_AGG]]
- → [[ADM_HANDSET_HIST_AGG]]

