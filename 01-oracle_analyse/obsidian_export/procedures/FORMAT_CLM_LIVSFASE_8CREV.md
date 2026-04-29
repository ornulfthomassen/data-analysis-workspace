# FORMAT_CLM_LIVSFASE_8CREV

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle function maps Norwegian life-stage descriptive strings (e.g., 'Barn', 'Ungdom') to corresponding numeric identifiers. It takes a VARCHAR2 input and returns a NUMBER, with specific mappings for known life stages, NULL for 'Ukjent' or NULL input, and -9999 for unrecognized values. The commented-out SQL suggests these mappings are derived from a 'Livsfase CLM' model within a segment dimension.

