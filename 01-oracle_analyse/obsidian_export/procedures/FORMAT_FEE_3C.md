# FORMAT_FEE_3C

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Categorizes a numeric input (P_IN) into specific string ranges based on its value. It returns 'Ukjent' for NULL, 'Under 199' for values less than 200, '200-349' for values between 200 and 349 (inclusive), and 'Over 349' for values greater than 349. The returned string is trimmed.

