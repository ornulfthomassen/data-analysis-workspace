# MOVIE_RENTAL_AVTALE_V_DEV

**Schema:** `CCM` | **Type:** `View`

## Description
This view creates a comprehensive dataset of movie rental agreements by joining core agreement data with customer, product, and status information. It enriches the raw data by deriving new attributes such as provider details, film format (3D/HD/SD), customer segments (e.g., VIP, test customer), and various status descriptions, while applying specific filters based on agreement status, date, and product library names.

## Data Sources (Inputs)
- ← [[KAS.avtale]]
| Column Name |
|---|
| avtale_nr |
| status |
| abonnent_nr |
| produkt_nr |
| enhets_pris |
| rabatt |
| fra_dato |
| reg_dato |
| rabatt_kr |
| signatur |
- ← [[KAS.kunde]]
| Column Name |
|---|
| abonnent_nr |
| PURREKODE |
| kundegruppe |
- ← [[KAS.produkt_vod]]
| Column Name |
|---|
| bibliotek_navn |
| film_id |
| platform |
| pris |
| produkt_nr |
| tittel |
| behandlet |
| dato_i_tabell |
- ← [[KAS.FSO_KAS_STATUS]]
| Column Name |
|---|
| status |
| KATEGORI_BESKRIVELSE |
| PRODUKT_NR |

