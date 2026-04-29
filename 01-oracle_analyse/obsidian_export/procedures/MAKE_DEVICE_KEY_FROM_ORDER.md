# MAKE_DEVICE_KEY_FROM_ORDER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This function takes an International Mobile Equipment Identity (IMEI) string as input. It trims whitespace from the IMEI, extracts a substring by removing the last 7 characters (which typically represents the Type Allocation Code - TAC), converts this substring to a number, and returns it. If the conversion or extraction fails, it returns -1.

