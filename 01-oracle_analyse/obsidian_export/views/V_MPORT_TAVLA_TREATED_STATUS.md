# V_MPORT_TAVLA_TREATED_STATUS

**Schema:** `CCM` | **Type:** `View`

## Description
This view counts distinct main numbers (likely representing orders or subscribers) based on their order arrival date, service provider, and order status. It categorizes these counts based on whether a corresponding campaign contact (from specific campaign groups) exists in the dialog history since the order arrival date. Specifically, it distinguishes between 'Ubehandlet' (Untreated) and 'Behandlet' (Treated) states regarding campaign involvement, excluding specific service providers ('Talkmore', 'Dipper').

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.V_MPORT_TAVLA]]
- ← [[CLM_CCM.CCM_DIALOG_HISTORY]]
- ← [[CRM_ANALYSE.KIM_CAMPAIGN_DIM]]

