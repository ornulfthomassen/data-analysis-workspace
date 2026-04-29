# FORMAT_SERVICE_PROVIDER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This is an Oracle SQL function named `FORMAT_SERVICE_PROVIDER`. It takes a numeric input (P_IN) representing a service provider ID and returns a VARCHAR2 string, which is the corresponding service provider's name. It acts as a lookup or mapping utility, translating numeric codes into descriptive text, with specific handling for NULL, -1, -2, and various other numeric IDs, defaulting to 'Andre' if no match is found. The function primarily uses a CASE statement for this mapping.

