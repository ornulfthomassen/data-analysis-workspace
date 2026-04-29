# MAKE_DEVICE_KEY_FROM_LIVE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Extracts the Type Allocation Code (TAC) as a numeric value from a provided IMEI string. It assumes the input IMEI string has already had its last digit removed (making it 14 characters long typically), and then it further truncates the string to its first 8 characters before attempting to convert this substring into a number. Returns -1 if the conversion fails.

