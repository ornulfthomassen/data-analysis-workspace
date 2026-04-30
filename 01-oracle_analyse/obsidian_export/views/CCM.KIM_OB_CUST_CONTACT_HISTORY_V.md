# KIM_OB_CUST_CONTACT_HISTORY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named KIM_OB_CUST_CONTACT_HISTORY_V, retrieves outbound customer contact history from the past week (SYSDATE - 7 to SYSDATE + 1). It enriches this history with details about the cell package, campaign, communication, treatment, subscription, and associated handset information. Crucially, it filters out any contact records that have already been recorded in the `KIM_CAMPAIGN_DETAIL_FACT` table for outbound campaigns within the same timeframe, essentially providing an incremental or delta set of recent outbound campaign contacts.

## Data Sources (Inputs)
- ← [[CICDM.CI_CUST_CONTACT_HISTORY]]
| Column Name |
|---|
| KURT_ID |
| CONTACT_DTTM |
| CELL_PACKAGE_SK |

- ← [[CICDM.CI_CELL_PACKAGE]]
| Column Name |
|---|
| CELL_PACKAGE_SK |
| PACKAGE_SK |
| CAMPAIGN_SK |
| COMMUNICATION_SK |
| CHANNEL_CD |

- ← [[CICDM.CI_PACKAGE_X_TREATMENT]]
| Column Name |
|---|
| PACKAGE_SK |
| CONTRIBUTING_CELL_PACKAGE_SK |
| SEQUENCE_NO |
| TREATMENT_SK |

- ← [[CICDM.CI_SUBS_CONTACT_HISTORY]]
| Column Name |
|---|
| KURT_ID |
| CELL_PACKAGE_SK |
| CONTACT_DTTM |
| SUBSCRIPTION_ID |

- ← [[CCDW.SUBSCRIPTION]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| START_DATE |
| END_DATE |
| KURT_ID_PAYER |
| KURT_ID_USER |
| PRODUCT_OFFER_ID |
| BINDING_START_DATE |
| BINDING_END_DATE |

- ← [[CCDW.SUBSCRIPTION_HANDSET]]
| Column Name |
|---|
| SUBSCRIPTION_ID |
| TERMINAL_USE_FIRST_DATE |
| TERMINAL_USE_LAST_DATE |
| TAC_ID |

- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DETAIL_FACT]]
| Column Name |
|---|
| KURT_ID_OWNER |
| CONTACT_DTTM |
| CELL_PACKAGE_SK |
| SOURCE_SYSTEM_KEY |
| CONTACT_DATE_KEY |


