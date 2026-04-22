# GCP_EMAIL_SUBSCRIPTION_INFO

**Schema:** `CCM` | **Type:** `View`

## Description
This view identifies active email subscriptions that are categorized as 'Abonnement' (Subscription) and do not have an associated active or recently active 'Tilleggstjeneste' (Add-on service) specifically marked as 'Abonnementsavslutning' (Subscription termination). It extracts the subscription ID and the online email address for these qualifying subscriptions. In essence, it provides a list of active email subscriptions that are not currently under a termination process or have not been terminated very recently.

## Data Sources (Inputs)
- ← [[CCDW.SUBSCRIPTION]]
- ← [[GALAXY.PRODUCT_DIM]]
- ← [[CCDW.SUBSCRIBED_PRODUCT]]

