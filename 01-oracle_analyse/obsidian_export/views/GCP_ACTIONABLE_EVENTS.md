# GCP_ACTIONABLE_EVENTS

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides event data used for customer interactions, specifically for transferring CLM (Customer Lifecycle Management) activities from RTDM to SAS360. It defines a subject level customer for an infomap and is tentatively used by HighTouch. It filters out certain trigger IDs and only includes events processed within the last 14 days. The view transforms and casts various input fields from a source history table into a standardized format for actionable events, including customer identifiers, unit details, resource information, timestamps, and several event-specific value/date fields with dynamic descriptions based on trigger IDs.

## Data Sources (Inputs)
- ← [[CLM_RTDM.ESP_TRIGGER_HISTORY]]

