# FORMAT_BINDING_4C

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This PL/SQL function categorizes a numeric input value (P_IN), likely representing days relative to an expiration date, into one of several descriptive 'binding status' strings. The categories are: 'Aldri binding' (Never bound), 'Binding utløpt' (Binding expired), 'Bindingsutløp' (Binding expiration), or 'I binding' (Currently bound), with an 'ERROR' fallback.

