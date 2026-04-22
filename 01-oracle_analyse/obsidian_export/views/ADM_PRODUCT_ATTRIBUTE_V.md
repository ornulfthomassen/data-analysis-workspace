# ADM_PRODUCT_ATTRIBUTE_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, ADM_PRODUCT_ATTRIBUTE_V, is designed to provide a standardized set of product attributes by consolidating information from primary product dimensions and historical attribute data. Its main functions include:
1.  **Standardizing and Converting Attributes**: It extracts various product-related details (like included minutes, SMS, MMS, data, fees, baud rates) from text-based fields, converts them into numerical formats (e.g., MB, Mbps), and handles different units (KB, MB, GB, Kbps, Mbps) and special string values ('FRI BRUK', 'Ubegrenset', 'UNLIMITED').
2.  **Applying Business Logic**: It implements specific business rules for deriving or overriding attributes such as `DRM_COMMON_BRAND` (e.g., setting 'Service Provider' for Wholesale customers), `PRODUCT_FAMILY`, and complex calculations for `INCLUDED_MB` and `BAUD_REDUCTION_QUOTA_MB` based on various product characteristics.
3.  **Merging and Defaulting**: It joins current product data with `CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST` (filtered for `CURRENT_STATUS = 'Y'`) to fill in missing (NULL) values, ensuring that a comprehensive set of current or historical default attributes is available.
4.  **Data Filtering**: It filters out products originating from specific source systems ('Marius', 'K2') to focus on relevant product data.

## Data Sources (Inputs)
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CLM_ADM.ADM_PRODUCT_ATTRIBUTE_HIST]]

