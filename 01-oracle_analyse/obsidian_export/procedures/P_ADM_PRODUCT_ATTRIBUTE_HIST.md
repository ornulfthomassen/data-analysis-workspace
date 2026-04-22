# P_ADM_PRODUCT_ATTRIBUTE_HIST

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
The procedure implements Slowly Changing Dimension (SCD) Type 2 logic for product attributes. It compares current product attribute data from a source view (`CLM_ADM.ADM_PRODUCT_ATTRIBUTE_V`) with existing historical product attributes (`CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST`). For products whose attributes have changed, it marks the old historical record as inactive and inserts a new, active record. For entirely new products, it inserts a new active record. It also creates a temporary backup table (`TMP_PRODUCT_ATTR_HIST_BCK`) of the active historical records at the beginning of the process, which is subsequently dropped.

## Data Sources (Inputs)
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_V]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]

## Target Tables (Outputs)
- → [[ADM_PRODUCT_ATTRIBUTE_HIST]]
- → [[TMP_PRODUCT_ATTR_HIST_BCK]]

