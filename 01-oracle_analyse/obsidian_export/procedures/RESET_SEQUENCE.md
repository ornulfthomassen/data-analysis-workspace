# RESET_SEQUENCE

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
Resets an Oracle database sequence (identified by SEQ_NAME) so that its next generated value will be 1, regardless of its previous state. This is achieved by temporarily setting its MINVALUE to 0, adjusting its INCREMENT BY value to effectively 'skip' to 0, consuming a NEXTVAL to make its current value 0, and then restoring its INCREMENT BY to 1.

