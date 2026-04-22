# VYA_CUSTOMER_ACTIVITY_LOG

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to consolidate, standardize, and anonymize customer activity log data. It extracts core activity details such as customer surrogate key, event date, event ID, and various levels of event categorization. A significant part of its functionality involves extensive cleansing and anonymization of event descriptions, replacing sensitive information (like numbers, T-signs, email addresses, URLs) with generic placeholders and standardizing common event phrases. It also maps customer identifiers to a surrogate key, potentially generating a negative ID for unmapped customers, for use in data analysis or business intelligence platforms like Viya/Mjøsa.

## Data Sources (Inputs)
- ← [[CUSTOMERLOG.ACTIVITY_LOG]]
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER_LINK]]
- ← [[CUSTOMERLOG.INTERNAL_CUSTOMER]]
- ← [[CM.CUSTOMER]]
- ← [[CUSTOMERLOG.ACTIVITY_DESCRIPTION]]
- ← [[CUSTOMERLOG.ACTIVITY_EVENT]]
- ← [[CLM_ADM.ADM_CUSTOMER_MAPPING]]

