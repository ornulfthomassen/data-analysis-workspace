# P_ADR_ODS_MSISDN_SERVICE_PROVIDER

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure P_ADR_ODS_MSISDN_SERVICE_PROVIDER creates and maintains a 'universe' of MSISDNs (Mobile Station International Subscriber Directory Numbers) by extracting and transforming subscription and customer data. It categorizes each MSISDN by its current status, service type ('MOBIL'), service provider (e.g., Telenor, Talkmore, Dipper), and Telenor division (CONSUMER or BUSINESS). The process uses a full refresh (fulload) methodology implemented through a table swapping mechanism. It first populates a new staging table, then validates the data volume against the existing production table. If acceptable, it renames the current production table to a backup, and renames the new staging table to become the new production table. It also manages indexes and grants select privileges. The resulting data is intended for downstream use cases such as telemarketing and lead generation.

## Data Sources (Inputs)
- ← [[CM.SUBSCRIPTION]]
- ← [[CM.CUSTOMER]]
- ← [[ALL_INDEXES]]

## Target Tables (Outputs)
- → [[ODS_MSISDN_SERVICE_PROVIDER]]
- → [[ODS_MSISDN_SERVICE_PROVIDER_N]]

