# SAME_CHANNEL_CHECK

**Schema:** `CRM_ANALYSE` | **Type:** `Procedure`

## Description
Evaluates input channel and dealer attributes against a set of predefined business rules specific to an 'original version' check. It returns '1' if the combination of attributes matches any of the specified criteria (e.g., 'MINE SIDER' channel with specific dealer names, 'ELECTRONIC' channel with specific dealer names, 'POINT OF SALE BRANCH' with 'TELENORBUTIKKEN NORGE' chain, or 'CALL CENTER' with 'KS' sales channel description), and '0' otherwise. The function only performs this check if the 'CHECK_TYPE' input parameter is 'O'.

