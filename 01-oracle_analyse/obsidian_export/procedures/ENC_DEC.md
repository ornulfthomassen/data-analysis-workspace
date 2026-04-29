# ENC_DEC

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This Oracle PL/SQL package body implements encryption and decryption functions. It uses the DBMS_CRYPTO package to encrypt and decrypt VARCHAR2 data into RAW format and vice-versa, utilizing DES encryption with CBC chaining and PKCS5 padding, and a predefined encryption key.

