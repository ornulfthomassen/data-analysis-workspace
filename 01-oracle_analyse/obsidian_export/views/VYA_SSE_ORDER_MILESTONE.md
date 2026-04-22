# VYA_SSE_ORDER_MILESTONE

**Schema:** `CCM` | **Type:** `View`

## Description
This view transforms order-related milestone data from a row-based format into a column-based format for specific milestone IDs. It consolidates details (name, actual date, baseline date, planned date, state, and comments) for milestones with IDs 14, 102, and 290 for each order ('OBJECTTYPE = 'Orders''), presenting them as separate columns to provide a comprehensive, single-row overview of these key milestones per order.

## Data Sources (Inputs)
- ← [[KAPAKS.SSE_MILESTONE]]

