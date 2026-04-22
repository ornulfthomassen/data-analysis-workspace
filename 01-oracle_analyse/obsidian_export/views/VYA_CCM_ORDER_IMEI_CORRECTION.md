# VYA_CCM_ORDER_IMEI_CORRECTION

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and tracks corrections made to IMEI (International Mobile Equipment Identity) numbers within agreement orders. It links a 'correction' agreement order (ACTION_TYPE_ID = 'CH') to an 'original' agreement order for the same agreement. For each correction, it extracts the old IMEI and the new IMEI, along with the corresponding agreement order IDs and timestamps for both the original order and the correction.

## Data Sources (Inputs)
- ← [[ONL_REP.AGREEMENT_ORDER]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMPONENT]]
- ← [[ONL_REP.AGREEMENT_ORDER_COMP_PARAM]]

