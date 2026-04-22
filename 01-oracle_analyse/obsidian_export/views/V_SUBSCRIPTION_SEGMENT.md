# V_SUBSCRIPTION_SEGMENT

**Schema:** `CCM` | **Type:** `View`

## Description
This view, V_SUBSCRIPTION_SEGMENT, serves as a direct passthrough or an alias for the CCDW_SEGMENT.SUBSCRIPTION_SEGMENT table or view. It provides access to all columns (SEGMENT_ID, MODEL_ID, SUBSCRIPTION_ID, START_DATE, END_DATE, RUN_ID, SEQ_ID) of the source object without any transformations, aggregations, or filtering. Its primary purpose is likely to expose the underlying subscription segment data to the CRM_ANALYSE schema, potentially for access control, schema abstraction, or simplification of object names within that schema.

## Data Sources (Inputs)
- ← [[CCDW_SEGMENT.SUBSCRIPTION_SEGMENT]]

