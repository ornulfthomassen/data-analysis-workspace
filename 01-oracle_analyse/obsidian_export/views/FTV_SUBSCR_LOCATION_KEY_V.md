# FTV_SUBSCR_LOCATION_KEY_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view is designed to determine or impute a canonical 'INSTALL_LOCATION_KEY' for subscriptions. It uses a multi-step process (four distinct methods combined with UNION ALL) to derive this key, often aiming to resolve ambiguous, missing, or less specific location keys (e.g., street addresses) to more precise apartment-specific location identifiers. The final output for each subscription is the maximum of the derived 'INSTALL_LOCATION_KEY' candidates from these methods.

## Data Sources (Inputs)
- ← [[FTV_MISSING_FAR_ID_TMP]]
- ← [[SUBSCRIPTION_DIM]]
- ← [[FTV_MAP_APARTMENT_LOC_KEY]]
- ← [[LOCATION_DIM]]

