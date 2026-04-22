# KIM_CONTACT_HANDSET_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, `KIM_CONTACT_HANDSET_DIM_V`, acts as a wrapper around the `KIM_HANDSET_DIM_V` view. Its primary purpose is to expose handset dimension data, essentially selecting all columns from `KIM_HANDSET_DIM_V` while specifically renaming the `HANDSET_KEY` column to `CONTACT_HANDSET_KEY`. This renaming suggests its use in a context where handset information needs to be linked or presented from the perspective of a contact, or to align with a specific naming convention within a contact-related data model.

## Data Sources (Inputs)
- ← [[CRM_ANALYSE.KIM_HANDSET_DIM_V]]

