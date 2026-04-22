# VYA_DEALER_DIM

**Schema:** `CCM` | **Type:** `View`

## Description
This view (`VYA_DEALER_DIM`) serves as a Dealer Dimension, primarily transforming and standardizing dealer-related attributes by selecting all columns from the `GALAXY.DEALER_DIM` source table. Its main purpose is to cast various columns to specific data types and lengths, and in some cases, rename them (e.g., sales channel descriptions), making the data suitable for a data warehouse or reporting environment. It provides comprehensive details about dealers including identifiers, names, types, addresses, status, associated employees, sales channel information, and geographical coordinates.

## Data Sources (Inputs)
- ← [[GALAXY.DEALER_DIM]]

