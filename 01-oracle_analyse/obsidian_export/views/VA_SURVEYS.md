# VA_SURVEYS

**Schema:** `CLM_ADM` | **Type:** `View`

## Description
This view consolidates and standardizes data from various Qualtrics surveys, providing a comprehensive dataset of survey results for analysis. It combines survey metadata, questions, and different types of answers (headings, single-choice, multi-choice, free-text comments, and Net Promoter Score classifications) with extensive respondent demographic, device, and customer journey information. The purpose is to prepare survey data for consumption by analytical systems like SAS Viya/InMemory Analytics for Customer Lifecycle Management (CLM).

## Data Sources (Inputs)
- ← [[NPS.SURVEYS]]
- ← [[NPS.SURVEY_ANSWER_META]]
- ← [[NPS.SURVEY_QUESTIONS]]
- ← [[NPS.SURVEY_ANSWER]]
- ← [[NPS.SURVEY_QUESTION_CHOICES]]

