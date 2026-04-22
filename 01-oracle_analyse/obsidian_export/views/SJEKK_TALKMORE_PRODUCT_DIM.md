# SJEKK_TALKMORE_PRODUCT_DIM

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view identifies and categorizes new and changed 'Talkmore' primary product dimension records. It compares the current state of 'Talkmore' products (derived from `FINANCE_MART.PRODUCT_DIM_V` with specific business rules applied) against a reference table (`CLM_ADM.TALKMORE_PRIM_PRODUCT_DIM`). The output indicates whether a record is 'new', or if an existing record has 'changed' (showing both the old and new versions of the change). It essentially provides a delta or audit log for 'Talkmore' product master data.

## Data Sources (Inputs)
- ← [[FINANCE_MART.PRODUCT_DIM_V]]
- ← [[CLM_ADM.TALKMORE_PRIM_PRODUCT_DIM]]

