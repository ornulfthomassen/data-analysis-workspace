# MOVIE_RENTAL_MAIN_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
Provides a consolidated view of movie rental transactions, calculating detailed financial metrics such as provider revenue share (`PROVIDER_CUT`, `SUM_TO_PROVIDER`, `REV_SHARE`), product pricing (`PRODUCT_PRICE`, `SALES_PRICE`), and content age (`OLDER_THAN_180_DAYS`, `OLDER_THAN_90_DAYS`). It categorizes assets (`ASSET_TYPE`) and combines data from rental agreements, product information, campaign and exception rules, and content licensing details from various CMS sources. The view aggregates total amounts and number of movies for unique rental product/asset combinations.

## Data Sources (Inputs)
- ← [[CCM.MOVIE_RENTAL_AVTALE_V_DEV]]
- ← [[QLIKVIEW.PRODUKT]]
- ← [[QLIKVIEW.FILM_kampanje]]
- ← [[QLIKVIEW.FILM_Unntak]]
- ← [[QLIKVIEW.FILM_FørsteGratis]]
- ← [[KAS.CMS_MOVIE]]
- ← [[QLIKVIEW.TV_CMS_MEDIA_ASSET]]
- ← [[KAS.CMS_EPISODE]]

