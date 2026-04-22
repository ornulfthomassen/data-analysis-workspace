# VYA_FTV_KAS_LOC_SUB_KEY

**Schema:** `CCM` | **Type:** `View`

## Description
This view consolidates subscription information, providing a mapping from `USER_LOCATION_KEY` to its 'Bredbånd' (broadband) and 'TV' subscription keys and associated KAS (Kabel-TV Abonnement System) subscriber numbers. It identifies locations that have a single distinct subscription key for a given service category, considering both all subscriptions and only active ones, and then pivots these subscription details into dedicated columns for each service type.

## Data Sources (Inputs)
- ← [[GALAXY.SUBSCRIPTION_DIM]]

