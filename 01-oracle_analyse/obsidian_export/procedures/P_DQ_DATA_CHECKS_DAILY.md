# P_DQ_DATA_CHECKS_DAILY

**Schema:** `CCM` | **Type:** `Procedure`

## Description
This procedure performs a series of daily data quality (DQ) checks by calculating aggregated reservation numbers (TM and DM for Brsund and Telenor regions) from the `CLM_CCM.CCM_CUSTOMER_V` view. The results of these checks are then inserted as individual records into the `DQ_DATA_CHECKS` table, detailing the data category, source checked, master source, measure code, check timestamp, and the numerical result.

## Data Sources (Inputs)
- ← [[CLM_CCM.CCM_CUSTOMER_V]]
| Column Name |
|---|
| RES_BRSUND_TM |
| RES_BRSUND_DM |
| RES_TELENOR_TM |
| RES_TELENOR_DM |

## Target Tables (Outputs)
- → [[DQ_DATA_CHECKS]]
| Column Name |
|---|
| DATA_CATEGORY |
| SOURCE_CHECKED |
| SOURCE_MASTER |
| MEASURE_CD |
| MEASURE_CHECK_DTTM |
| MEASURE_RESULT_NUM |
| MEASURE_RESULT_DATE |
| MEASURE_RESULT_TXT |
| MEASURE_SQL |

