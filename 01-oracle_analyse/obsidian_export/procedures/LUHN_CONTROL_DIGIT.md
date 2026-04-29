# LUHN_CONTROL_DIGIT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Calculates the Luhn control digit for a given input string. The function first removes all non-digit characters from the input and reverses the resulting string. It then iterates through the reversed digits, doubling every second digit (starting from the first digit on the left, which corresponds to the rightmost digit of the original number). If a doubled digit's value is 10 or greater (e.g., 7 doubled is 14), its individual digits are summed (e.g., 1+4=5). Finally, it sums all the processed digits and calculates the check digit required to make this total sum a multiple of 10.

