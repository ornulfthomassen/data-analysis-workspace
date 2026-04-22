# NEW_MPP_INVOICE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view aggregates and categorizes recent invoice data from specific source systems and market areas. It calculates total data volume and gross amount, determines an overall invoice status based on line item types, and breaks down the gross amount into specific categories such as 'ENGANGSPRISER', 'FASTE PRISER', 'TELENOR SWAP', and 'BRUK'. The data is summarized per invoice (identified by various KURT_IDs and Subscription ID) and invoice date, focusing on records from the last 4 days.

## Data Sources (Inputs)
- ← [[CCDW_INVOICE.INVOICE_DETAIL]]
- ← [[GALAXY.INVOICE_LINE_TYPE_DIM_V]]

