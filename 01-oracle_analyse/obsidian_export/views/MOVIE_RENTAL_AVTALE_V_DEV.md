# MOVIE_RENTAL_AVTALE_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and transforms movie rental agreement data from various KAS schema tables. It enriches agreement details with customer type flags (VIP, test customer), standardizes content library names, extracts film IDs, classifies movies by format (3D, HD, SD), and incorporates agreement status information. The view filters agreements based on specific dates (after 2013-01-01), status codes, and a predefined list of content providers/bibliotek names.

## Data Sources (Inputs)
- ← [[KAS.avtale]]
- ← [[KAS.kunde]]
- ← [[KAS.produkt_vod]]
- ← [[KAS.FSO_KAS_STATUS]]

