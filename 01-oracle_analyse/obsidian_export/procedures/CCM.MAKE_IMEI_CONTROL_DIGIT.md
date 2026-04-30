# MAKE_IMEI_CONTROL_DIGIT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This PL/SQL function calculates and returns an IMEI (International Mobile Equipment Identity) number with its control digit. It takes a numeric part of an IMEI as input, validates its length (expected to be 13 or 14 digits), and then applies a checksum algorithm (resembling the Luhn algorithm) to generate the control digit. This control digit is appended to the original number, and the result is padded with leading zeros to a total length of 15 characters. The function handles invalid input (NULL or incorrect length) by returning specific error strings ('UKJENT' or 'UGYLDIG').

