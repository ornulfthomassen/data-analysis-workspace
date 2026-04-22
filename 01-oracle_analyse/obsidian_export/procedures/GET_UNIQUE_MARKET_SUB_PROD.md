# GET_UNIQUE_MARKET_SUB_PROD

**Schema:** `CLM_ADM` | **Type:** `Procedure`

## Description
This Oracle SQL function, named `GET_UNIQUE_MARKET_SUB_PROD`, takes an input string. It first initializes an output string with the first word of the input, converted to uppercase and cleaned. Then, it iterates through all space-separated words in the input string (also converted to uppercase). For each word, it checks if that word is already present in the output string. If the word is unique (not yet in the output string), it appends an underscore `_` followed by the word to the output string. Finally, it returns the concatenated string of unique, uppercase words, delimited by underscores. The overall purpose is to extract, normalize, and aggregate unique keywords from a phrase.

## Data Sources (Inputs)
- ← [[DUAL]]

