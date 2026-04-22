# GCP_MOBILMERKET_RESPONSE

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates participant and answer data for the 'Mobilmerket' service, specifically for loading into Google Cloud Platform (GCP) BigQuery for reporting purposes. It joins participant details with their responses, and the IP address is hashed for privacy.

## Data Sources (Inputs)
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_ANSWER]]
- ← [[THIRD_PARTY_SERVICES.MOBILMERKET_PARTICIPANT]]

