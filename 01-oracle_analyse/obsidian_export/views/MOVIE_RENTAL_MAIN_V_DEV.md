# MOVIE_RENTAL_MAIN_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates and transforms movie rental data, calculating various financial metrics (product price, sales price, provider cut, revenue share) and business rules (asset type, age of content, campaign applicability, exceptions). It unifies information from rental agreements, product details, campaign/exception rules, and content management systems to provide a comprehensive overview of movie rentals.

## Data Sources (Inputs)
- ← [[CCM.MOVIE_RENTAL_AVTALE_V_DEV]]
| Column Name |
|---|
| avtale_nr_avtale |
| reg_dato_avtale |
| bibliotek_navn_prodvod |
| film_id_prodvod |
| film_id |
| produkt_nr_avtale |
| abonnent_nr_avtale |
| enhets_pris_avtale |
| TITLE |
| NUMBER_OF_MOVIES |
| JA_NEI_3D |
- ← [[QLIKVIEW.PRODUKT]]
| Column Name |
|---|
| produkt_nr |
| ut_pris |
| notat |
- ← [[QLIKVIEW.FILM_kampanje]]
| Column Name |
|---|
| ASSET_ID |
| RESOLUTION |
| PROVIDER |
| PERIODE_FRA |
| PERIODE_TIL |
| Kampanje |
| KAMPANJE_NUM |
| OVERSTYRT_PROVIDERCUT |
- ← [[QLIKVIEW.FILM_Unntak]]
| Column Name |
|---|
| ASSET_ID |
| RESOLUTION |
| PROVIDER |
| PERIODE_FRA |
| PERIODE_TIL |
| PROVIDER_CUT |
- ← [[QLIKVIEW.FILM_FørsteGratis]]
| Column Name |
|---|
| provider |
| PERIODE_FRA |
| PERIODE_TIL |
- ← [[KAS.CMS_MOVIE]]
| Column Name |
|---|
| TELENOR_COMMON_ID |
| LICENSE_START_NO |
- ← [[QLIKVIEW.TV_CMS_MEDIA_ASSET]]
| Column Name |
|---|
| ORIGINAL_ASSET_ID_MA |
| video_asset_available_from_ma |
- ← [[KAS.CMS_EPISODE]]
| Column Name |
|---|
| TELENOR_COMMON_ID |
| LICENSE_START_NO |

