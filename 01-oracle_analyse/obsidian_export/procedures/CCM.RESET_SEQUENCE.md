# RESET_SEQUENCE

**Schema:** `CCM` | **Type:** `Procedure`

## Description
The procedure `RESET_SEQUENCE` is designed to reset an Oracle database sequence (specified by `SEQ_NAME` parameter) so that its next generated value (`NEXTVAL`) will be 1. It achieves this by temporarily manipulating the sequence's `MINVALUE` and `INCREMENT BY` properties to force the internal current value to 0, then increments it to 1 with a `NEXTVAL` call, and finally restores the `INCREMENT BY` value to 1. This involves direct DDL operations on the sequence object itself.

