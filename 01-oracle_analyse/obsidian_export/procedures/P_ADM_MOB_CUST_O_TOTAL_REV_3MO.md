# P_ADM_MOB_CUST_O_TOTAL_REV_3MO

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL procedure, `P_ADM_MOB_CUST_O_TOTAL_REV_3MO`, calculates and aggregates mobile customer ownership total revenue for a specified month (`V_YYYYMM`). It performs a multi-step process: First, it dynamically creates a temporary table (`TMP_MOB_CUST_O_TOTAL_REV_3MO`) which stores the aggregated revenue data, customer information, and subscription details from various source tables. This temporary table is created using a complex SELECT statement that groups data by customer and calculates various metrics like net revenue, number of subscriptions, and product type counts. After populating the temporary table, the procedure checks for the existence of a corresponding partition in the main target table (`ADM_MOB_CUST_O_TOTAL_REV_3MO`). If the partition does not exist, it creates it. Finally, it uses an `ALTER TABLE ... EXCHANGE PARTITION` statement to efficiently move the data from the temporary table into the specific partition of the permanent, partitioned target table. The procedure also handles error logging, statistics gathering, and grants SELECT privileges on the updated target table. It includes checks for source data availability and prevents overwriting existing data if specified.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_MOB_SUBS_REVENUE_3MO]]
- ← [[CLM_ADM.ADM_MOB_SUBSCRIPTION_CORE]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]
- ← [[GALAXY.DATE_DIM_MV]]

## Target Tables (Outputs)
- → [[TMP_MOB_CUST_O_TOTAL_REV_3MO]]
- → [[ADM_MOB_CUST_O_TOTAL_REV_3MO]]

