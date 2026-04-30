# P_CCM_USER_SERVICES_KURT

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure processes and consolidates user account, phone verification, and service access data from various source systems (Comoyo FIM, Galaxy, CM). It links users to a central 'kurt_id', identifies different verification sources ('HL', 'SDMV', 'CM'), aggregates this information, and finally assigns a 'QA_flag' based on the customer type and the combination of verification sources.

## Data Sources (Inputs)
- ← [[COMOYO.USER_SERVICES_SERVICE_SCD]]
| Column Name |
|---|
| USER_ID |
| END_DATE |
| START_DATE |
| SERVICE_FIRST_DATE |
| CURRENT_RECORD |

- ← [[COMOYO.FIM_USER_ACCOUNTS]]
| Column Name |
|---|
| USER_ID |
| ACC_USER_ID |
| ACC_MSISDN |

- ← [[COMOYO.FIM_USER_PHONES]]
| Column Name |
|---|
| USER_ID |
| PH_MSISDN |
| PH_VERIFICATION_TIME |
| PH_VERIFIED |

- ← [[GALAXY.SUBSCRIPTION_DIM_MV]]
| Column Name |
|---|
| COMOYO_USER_ID |
| MAIN_NUMBER |
| SUBSCRIPTION_KEY |
| CURRENT_STATUS |

- ← [[GALAXY.SUBSCR_DETAIL_FACT]]
| Column Name |
|---|
| SUBSCRIPTION_KEY |
| USER_CUSTOMER_KEY |
| PRIM_PROD_END_DT_KEY |

- ← [[CM.SUBSCRIPTION]]
| Column Name |
|---|
| DIRECTORY_NUMBER_ID |
| S212_PRODUCT_ID |
| CUST_ID_USER |
| SUBSCR_VALID_TO_DATE |
| INFO_IS_DELETED |

- ← [[CM.PROD_SERV_MAPPING]]
| Column Name |
|---|
| PRODUCT_UNIT_ID |
| PRODUCT_SERVICE_PROVIDER |

- ← [[CM.CUSTOMER]]
| Column Name |
|---|
| CUST_ID |
| KURT_ID |
| INFO_IS_DELETED |

- ← [[CLM_CCM.CCM_CUSTOMER]]
| Column Name |
|---|
| KURT_ID |
| CUSTOMER_TYPE_CD |

- ← [[CCM.CCM_USERS_TMP]]
| Column Name |
|---|
| USER_ID |

- ← [[CCM.CCM_PHONES_TMP]]
| Column Name |
|---|
| USER_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |

- ← [[CCM.CCM_HARDLINK_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |

- ← [[CCM.CCM_USERS_SDMV_TMP]]
| Column Name |
|---|
| USER_ID |
| MAIN_NUMBER |
| KURT_ID |
| VERIFISERT |

- ← [[CCM.CCM_PHONES_CM_TMP]]
| Column Name |
|---|
| USER_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |
| KURT_ID |
| PRODUCT_SERVICE_PROVIDER |
| VERIFISERT |

- ← [[CCM.CCM_USER_KURT_SAMMEN_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| KILDE |
| SP |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |

- ← [[CCM.CCM_USER_KURT_KILDE_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| CUSTOMER_TYPE_CD |
| KILDE_LIST |


## Target Tables (Outputs)
- → [[CCM.CCM_USERS_TMP]]
| Column Name |
|---|
| USER_ID |
| LAST_ACCESS_TM |
| FIRST_ACCESS_TM |
| SERVICE_FIRST_DATE |
| NUMBER_OF_SERVICES |

- → [[CCM.CCM_PHONES_TMP]]
| Column Name |
|---|
| USER_ID |
| MSISDN |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |

- → [[CCM.CCM_HARDLINK_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |

- → [[CCM.CCM_USERS_SDMV_TMP]]
| Column Name |
|---|
| USER_ID |
| MAIN_NUMBER |
| KURT_ID |
| VERIFISERT |

- → [[CCM.CCM_PHONES_CM_TMP]]
| Column Name |
|---|
| USER_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |
| KURT_ID |
| PRODUCT_SERVICE_PROVIDER |
| VERIFISERT |

- → [[CCM.CCM_USER_KURT_SAMMEN_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |
| KILDE |
| SP |

- → [[CCM.CCM_USER_PHONE_KILDE_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| SP |
| MAIN_NUMBER |
| MAX_VERIFICATION_DTTM |
| CUSTOMER_TYPE_CD |
| KILDE_LIST |

- → [[CCM.CCM_USER_KURT_KILDE_TMP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| MAX_VERIFICATION_DTTM |
| CUSTOMER_TYPE_CD |
| KILDE_LIST |

- → [[CCM.CCM_USER_KURT_KILDE_CP]]
| Column Name |
|---|
| USER_ID |
| KURT_ID |
| MAX_VERIFICATION_DTTM |
| CUSTOMER_TYPE_CD |
| KILDE_LIST |
| QA_FLAG |


