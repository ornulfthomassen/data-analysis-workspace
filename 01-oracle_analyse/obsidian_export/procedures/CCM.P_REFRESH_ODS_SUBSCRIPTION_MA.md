# P_REFRESH_ODS_SUBSCRIPTION_MA

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Orchestrates the refresh of three Operational Data Store (ODS) materialized views: ODS_CUST_ROLE_SUBSCR_MV, ODS_SUBSCRIPTION_MV, and ODS_SUBSCRIBED_OFFER_MV. This typically involves recomputing their data from their respective base tables.

## Target Tables (Outputs)
- → [[CCM.ODS_CUST_ROLE_SUBSCR_MV]]
- → [[CCM.ODS_SUBSCRIPTION_MV]]
- → [[CCM.ODS_SUBSCRIBED_OFFER_MV]]

