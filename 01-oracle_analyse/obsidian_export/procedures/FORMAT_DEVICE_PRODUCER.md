# FORMAT_DEVICE_PRODUCER

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Standardizes device producer names by mapping various input string patterns (e.g., 'SAMSUNG', 'APPLE') to a consistent set of producer names like 'Samsung', 'Apple', 'Sony', etc. It returns 'Unknown' for NULL input and 'Other' for unrecognized inputs. The function operates purely on its input parameter and does not interact with any database tables.

