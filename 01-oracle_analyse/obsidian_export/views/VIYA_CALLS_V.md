# VIYA_CALLS_V

**Schema:** `CCM` | **Type:** `View`

## Description
Aggregates interaction data (calls) by various dimensions such as year/month, client, queue type, technical result, and inbound transfer group. It categorizes queue types into broader categories (e.g., 'Faktura', 'Teknisk') and filters data to include only interactions from 2022 onwards.

## Data Sources (Inputs)
- ← [[rsshugin.rm_ks_interaction]]
| Column Name |
|---|
| YEAR_MONTH |
| QUEUE_CLIENT |
| QUEUE_TYPE |
| TECHNICAL_RESULT |
| TRANSFER_INBOUND_GROUP |
| cal_date |

