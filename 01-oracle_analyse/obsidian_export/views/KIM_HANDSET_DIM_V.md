# KIM_HANDSET_DIM_V

**Schema:** `CCM` | **Type:** `View`

## Description
This view, named KIM_HANDSET_DIM_V, serves as a Handset Dimension for CRM analysis. Its primary function is to categorize handsets into 'MODEL_FAMILY' groups based on their manufacturer (Samsung, Apple, Sony, Nokia) and marketing name, providing a standardized family name for popular models (e.g., 'Galaxy S III Family', 'Sony Xperia Z1 Family', 'Nokia Lumia 800'). For other handsets, it defaults to the marketing name. Additionally, it selects a comprehensive set of handset specifications and technical details from an underlying handset dimension view.

## Data Sources (Inputs)
- ← [[GALAXY.HANDSET_DIM_V]]

