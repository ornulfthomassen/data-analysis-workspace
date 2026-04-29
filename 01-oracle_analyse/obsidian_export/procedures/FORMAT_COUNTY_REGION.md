# FORMAT_COUNTY_REGION

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
A PL/SQL function that translates a 2-character input code (presumably a county or municipality code) into a corresponding Norwegian regional name (e.g., 'Viken', 'Oslo', 'Innlandet'). It returns 'Ukjent' for NULL input and 'ERROR: [input]' for unrecognized codes.

