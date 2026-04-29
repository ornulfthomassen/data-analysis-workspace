# CCM_ENCRYPT_AES

**Schema:** `CCM` | **Type:** `Procedure`

## Description
Encrypts a given text string using AES256 encryption with a specified key. It utilizes `DBMS_CRYPTO` for the encryption process, converting the input text to RAW before encryption and then back to VARCHAR for the return value.

