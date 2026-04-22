# VYA_FTV_MISSING_FAR_ID

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies and determines the most appropriate installation location (INSTALL_LOC_KEY) and whether it's an apartment (IS_APARTMENT) for 'Fixed and TV' subscriptions that currently have a missing or default user location. It consolidates information from various source systems to resolve these missing location details for active subscriptions, prioritizing apartment locations where applicable.

## Data Sources (Inputs)
- ← [[CLM_ADM.FTV_MISSING_FAR_ID_TMP]]
- ← [[GALAXY.SUBSCRIPTION_DIM]]
- ← [[CCM.FTV_MAP_APARTMENT_LOC_KEY]]
- ← [[KAS.KUNDE]]
- ← [[KAS.ADRESSER]]
- ← [[GALAXY.LOCATION_DIM]]

