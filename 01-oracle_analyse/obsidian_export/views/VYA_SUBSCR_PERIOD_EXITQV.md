# VYA_SUBSCR_PERIOD_EXITQV

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates potentially overlapping or gappy individual subscription records into distinct, effective subscription periods for each subscription ID. It identifies the true start and end dates of these consolidated periods, assigns a sequential period number within each subscription, and flags the latest consolidated period for every subscription, specifically for a given source system (ID 42). This addresses a common 'Gaps and Islands' problem to rationalize subscription timelines.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]

