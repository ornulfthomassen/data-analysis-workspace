# MAKE_AGE_NR

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates the age (in full years) between a date of birth and a computation date. It performs validations on the input dates and only calculates the age if specific customer type and status conditions are met. If conditions are not met or inputs are invalid, it returns NULL. An error during execution returns -999999999.

