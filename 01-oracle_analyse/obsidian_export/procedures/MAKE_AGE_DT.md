# MAKE_AGE_DT

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates an age in years based on a date of birth and a computation date. It includes extensive validation for the input dates and only computes the age if the customer type and status codes match specific criteria. Returns NULL under various invalid input conditions or -999999999 on unhandled exceptions.

