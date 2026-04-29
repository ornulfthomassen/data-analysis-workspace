# IMEI_CONTROL_DIGIT2_CCDW

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Calculates the Luhn algorithm check digit for a given number, typically used for IMEI validation. It processes the input number digit by digit from right to left, applying specific arithmetic operations (doubling even-positioned digits and summing digits if the doubled value exceeds 9, adding odd-positioned digits as is) to derive a final check digit.

