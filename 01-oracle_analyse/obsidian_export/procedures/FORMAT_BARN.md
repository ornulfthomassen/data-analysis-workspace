# FORMAT_BARN

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
A PL/SQL function that translates a numeric input code (P_IN) representing child status (NULL, 0, or 1) into a human-readable Norwegian string ('Ukjent', 'Har barn', 'Har ikke barn' respectively). It returns 'ERROR' for any other numeric input.

