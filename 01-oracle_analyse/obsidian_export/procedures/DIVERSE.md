# DIVERSE

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
The Oracle package DIVERSE provides three overloaded functions, all named PREV_MONTH, to calculate and return a year-month identifier (YYYYMM) based on different input types. Specifically:
1.  PREV_MONTH(MAANED IN NUMBER): Takes a number representing a year-month (e.g., 202301) and returns the YYYYMM of the previous calendar month (e.g., 202212).
2.  PREV_MONTH(DATO IN DATE): Takes a date (e.g., '15-JAN-2023') and returns the YYYYMM of the previous calendar month (e.g., 202212).
3.  PREV_MONTH(DATO_STRENG IN VARCHAR2): Takes a date string in 'dd.mm.yyyy' format (e.g., '15.01.2023') and returns the YYYYMM of the day immediately preceding the input date (e.g., 202301 for '15.01.2023', or 202212 for '01.01.2023').

