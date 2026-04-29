# KS_INTERACTION_ORDERMATCH_P

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
This procedure acts as an orchestrator, sequentially calling three other stored procedures: CLM_KIM.KS_ORDER_LINES_REP_P, CLM_KIM.KS_INTERACTION_P, and KS_ENCRYPT_P. It manages transaction control by issuing a COMMIT after each sub-procedure call and logs the execution progress using DBMS_OUTPUT.

