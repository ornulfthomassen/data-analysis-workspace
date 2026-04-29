# DAYS_FROM_NOW

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Calculates the number of days between the month and day of an input date (P_DATE) and the current date (TRUNC(SYSDATE) or P_NOW), adjusting the result to reflect the closest occurrence of that month/day in relation to the current year's timeline, effectively determining 'days until/since this specific MMDD' while handling leap years and year rollovers.

