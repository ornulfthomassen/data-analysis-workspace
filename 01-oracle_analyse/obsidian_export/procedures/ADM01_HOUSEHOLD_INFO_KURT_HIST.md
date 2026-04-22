# ADM01_HOUSEHOLD_INFO_KURT_HIST

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This Oracle PL/SQL procedure is designed to maintain and populate a historical household information table named `ADM_HOUSEHOLD_INFO_KURT_HIST`. It first checks if the target table exists. If not, it creates the partitioned table with specified columns, indexes (unique and bitmap), and sets it to NOLOGGING mode. Subsequently, it determines the latest period to process (typically the previous month from SYSDATE). It then dynamically adds a new partition for this month if it doesn't already exist and inserts consolidated customer and household data from various `CLM_CCM` tables into the `ADM_HOUSEHOLD_INFO_KURT_HIST` table for that specific month. The procedure also gathers statistics on the table/partition and logs its execution status.

## Data Sources (Inputs)
- ← [[DUAL]]
- ← [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]
- ← [[CLM_CCM.CCM_CUSTOMER]]
- ← [[CLM_CCM.CCM_CUSTOMER_CONTACT_INFO]]
- ← [[CLM_CCM.CCM_HOUSEHOLD_INFO]]

## Target Tables (Outputs)
- → [[CRM_ANALYSE.ADM_HOUSEHOLD_INFO_KURT_HIST]]

