# FORMAT_COUNTY

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This is an Oracle SQL function named FORMAT_COUNTY. Its main purpose is to translate a two-digit county code (provided as an input string P_IN) into its corresponding Norwegian county name. It uses a CASE statement for this lookup, returning 'Ukjent' for NULL input, specific county names for known codes, and an 'ERROR' message for unmapped codes.

