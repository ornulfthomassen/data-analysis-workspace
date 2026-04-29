# VYA_SSE_ORDER_ROLE

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and pivots user and display name information for specific roles associated with 'Order' objects. It transforms multiple rows (each representing an object-role assignment) into a single row per order, with dedicated columns for the User ID and Display Name for each of the specified roles (CON-PL, CON-KAM, NP-FIBER, NR-SM, Project Manager).

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_OBJECTROLE]]
| Column Name |
|---|
| OBJECTID |
| ROLENAME |
| USERID |
| DISPLAYNAME |
| OBJECTTYPE |

