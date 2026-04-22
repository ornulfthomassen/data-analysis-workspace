# VYA_SSE_ORDER_ROLE

**Schema:** `CCM` | **Type:** `View`

## Description
Transforms and denormalizes order-related role assignments by pivoting role names into separate columns. For each unique order (OID), it displays the User ID and Display Name for specific roles ('CON-PL', 'CON-KAM', 'NP-FIBER', 'NR-SM', 'Project Manager') as distinct columns.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_OBJECTROLE]]

