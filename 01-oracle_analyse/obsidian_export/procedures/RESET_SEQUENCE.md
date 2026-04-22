# RESET_SEQUENCE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This procedure resets an Oracle sequence. It first sets the sequence's MINVALUE to 0. Then, it calculates an increment/decrement value based on the current sequence value (CURRVAL) to effectively bring the sequence's state close to 0. It applies this temporary increment/decrement, forces a NEXTVAL call to properly initialize the sequence (typically to 1), and finally resets the sequence's increment back to 1. The goal is to make the sequence start from 1 (or 0 if nextval after reset to 0 makes it 0) after its next call.

## Data Sources (Inputs)
- ← [[DUAL]]

