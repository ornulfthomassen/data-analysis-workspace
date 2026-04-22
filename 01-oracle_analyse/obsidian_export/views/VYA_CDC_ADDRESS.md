# VYA_CDC_ADDRESS

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and presents address details, including audit information and a specially formatted identifier (`FAR_ID_N`), by joining address data from `CDC.ADDRESS` with additional geographical information (`GRUNNKRETSNUMMER`) from `FAR.FARADR`. It also applies a filter to `FAR_ID` to be greater than 0.

## Data Sources (Inputs)
- ← [[CDC.ADDRESS]]
- ← [[FAR.FARADR]]

