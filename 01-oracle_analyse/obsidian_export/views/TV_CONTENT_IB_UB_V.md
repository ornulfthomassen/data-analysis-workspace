# TV_CONTENT_IB_UB_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view calculates and presents monthly 'Installed Base' (IB) and 'Usage Base' (UB) metrics for TV content. It aggregates content amounts by various dimensions (product, status, pricing, segment, customer type, decoder status) for specific periods: the beginning of each month and the most recent data point available ('MAX_PERIOD'). The 'IB' typically represents the installed base at the start of a given month, and 'UB' represents the installed base at the start of the subsequent month or the most current available base for the present month, facilitating period-over-period analysis of TV content subscriber or device base changes.

## Data Sources (Inputs)
- ← [[QLIKVIEW.TV_CONTENT_VOLUME]]

