# CTI_CONS_CUSTOMER_CDK_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view provides a filtered and de-duplicated list of consumer customer details. It selects various customer attributes such as customer number, type, IDs (KURT_ID, FAR_ID), contact numbers, address information, access type, and indicators for services like TV, broadband, and VoIP, along with status flags (STENGT, STENGT_STATUS, AKTIV). The data is filtered to include only records where the 'KURT_ID' is greater than 0. The GROUP BY clause on all selected columns ensures that only distinct combinations of these customer attributes are returned, effectively acting like a DISTINCT operation.

## Data Sources (Inputs)
- ← [[CCDW_CTI.CTI_CONS_CUSTOMER_CDK]]

