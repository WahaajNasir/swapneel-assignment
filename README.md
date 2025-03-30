# Mental Health Risk Prediction

This project aims to predict the likelihood of mental health concerns among individuals in a workplace setting, using a machine learning model based on survey data. The model uses various features related to employees' mental health awareness, support, and their personal experiences to predict whether they are at risk of mental health issues.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Installation Instructions](#installation-instructions)
- [Known Errors](#known-errors)
- [Dashboard Demo](#dashboard-demo)

## Project Overview

This project leverages a Random Forest Classifier trained on survey data to predict mental health risk. The model is designed to help organizations identify employees who might be at risk and offer timely support.

### Key Highlights:
- Predicts mental health risk using various employee-related features.
- Model trained using a cleaned dataset from the OSMI Mental Health in Tech Survey.
- Preprocessing, feature engineering, and imputation of missing values handled to ensure robust predictions.
- A Streamlit dashboard for real-time predictions and visualizations.

## Features

The following features are used for predicting mental health risk:
- **Are you self-employed?**
- **Employer Mental Health Benefits**
- **Knowledge of Mental Health Care Options**
- **Comfort Discussing Mental Health with Coworkers and Supervisors**
- **Past Mental Health Disorder History**
- **Current Mental Health Disorder**
- **Sought Treatment for Mental Health**
- **Age**
- **Gender**
- **Local or Online Resources for Mental Health**

These features are designed to provide insights into an employee's well-being and comfort level in seeking mental health support.

## Model Details
- **Algorithm Used:** Random Forest Classifier
- **Data Splitting:** 70% training, 30% testing
- **Evaluation Metrics:**
  - **Accuracy:** The accuracy of the model on the test set.
  - **Classification Report:** Includes precision, recall, and F1-score for each class (risk/no-risk).

The trained model is saved as a `.pkl` file and can be used for making predictions on new data.

## Dataset

The dataset used for training the model is the [OSMI Mental Health in Tech Survey](https://www.osmihelp.org/). The data consists of survey responses collected from employees in the tech industry regarding their experiences with mental health at work.

**Dataset columns used for training:**
- `Are you self-employed?`
- `employer_mh_benefits`
- `Do you know the options for mental health care available under your employer-provided coverage?`
- `Has your employer ever formally discussed mental health?`
- `Does your employer offer resources to learn more about mental health concerns and options for seeking help?`
- `Would you feel comfortable discussing a mental health disorder with your coworkers?`
- `Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?`
- `Do you think that discussing a mental health disorder with your employer would have negative consequences?`
- `Have you had a mental health disorder in the past?`
- `current_mental_disorder`
- `sought_treatment`
- `age`
- `gender`
- `Do you know local or online resources to seek help for a mental health disorder?`

## Installation Instructions

To set up the project on your local machine:

1. Clone this repository:


```bash
git clone https://github.com/WahaajNasir/swapneel-assignment.git
cd swapneel-assignment
```

## Known Errors
The visualizations contain some questions that cannot be visualized due to inconsistencies between the columns of the OSMI surveys between 2016 and 2017-2020. Some survey responses and columns are not consistent across the years, causing gaps in the visualizations for those questions. This issue will need to be addressed by normalizing the survey columns and ensuring consistency across different survey years.

## Streamlit App
The dashboard can be viewed at the following link:
https://mental-health-analysis-wahaaj.streamlit.app/

## Dashboard Demo
The dashboard demo can be viewed on the following youtube link:
https://youtu.be/EeCVkqqpAfU
