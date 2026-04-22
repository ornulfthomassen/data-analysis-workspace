# VYA_SURVEYS

**Schema:** `CCM` | **Type:** `View`

## Description
Consolidates and presents detailed results from Qualtrics surveys by combining survey metadata, question definitions, and various types of customer responses (including multiple-choice, open-ended comments, and Net Promoter Score classifications) into a single, unified view. It enriches the survey data with customer and device attributes, filtering for specific surveys and time periods, primarily for use by analytical tools like SAS Viya.

## Data Sources (Inputs)
- ← [[NPS.SURVEYS]]
- ← [[NPS.SURVEY_ANSWER_META]]
- ← [[NPS.SURVEY_QUESTIONS]]
- ← [[NPS.SURVEY_ANSWER]]
- ← [[NPS.SURVEY_QUESTION_CHOICES]]

