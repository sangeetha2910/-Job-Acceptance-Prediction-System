# HR Job Placement Prediction

## Data Science & Machine Learning Capstone Project

---

## 1. Project Overview

The **HR Job Placement Prediction** project is a Data Science and Machine Learning project designed to analyze candidate information and predict whether a candidate is likely to be **Placed** or **Not Placed**.

The project analyzes academic performance, technical skills, aptitude, communication, skills match, experience, certifications, job-role suitability, company tier, competition level, and other recruitment-related factors.

The project follows an end-to-end Data Science workflow:

**Data Understanding → Data Cleaning → EDA → Feature Engineering → Preprocessing → Machine Learning → Model Evaluation → Prediction → Dashboard → Business Insights**

---

## 2. Business Problem

HR teams need to evaluate a large number of candidates during recruitment. Manually analyzing candidate information can be time-consuming and may make it difficult to identify the factors that contribute to successful placement.

This project uses historical candidate data to identify placement patterns and build a Machine Learning model that can support HR decision-making.

---

## 3. Business Objective

The main objective is to develop a data-driven system that can:

- Predict candidate placement outcomes.
- Identify important factors influencing placement.
- Understand candidate strengths and weaknesses.
- Analyze recruitment and candidate patterns.
- Support data-driven candidate screening.
- Provide useful insights through a dashboard.

The model is intended as a **decision-support tool**, not as a replacement for human HR judgment.

---

## 4. Dataset Description

The project uses an **HR Job Placement Dataset** containing:

- **51,500 records**
- **26 columns**

The target variable is:

**`status`**

The target contains two outcomes:

- Placed
- Not Placed

Therefore, this project is a **Binary Classification** problem.

### Main Features

The dataset contains information related to:

- Academic performance
- Technical score
- Aptitude score
- Communication score
- Skills match percentage
- Certifications
- Years of experience
- Previous and expected CTC
- Employment gap
- Notice period
- Internship experience
- Relevant experience
- Company tier
- Job role match
- Competition level
- Relocation willingness
- Career switch willingness

---

## 5. Data Cleaning

Data cleaning was performed to improve the quality and reliability of the dataset.

The major steps included:

- Identifying and removing duplicate records.
- Identifying missing values.
- Handling missing categorical values.
- Performing logical consistency checks.
- Analyzing potential outliers.
- Validating data types and values.

A total of **1,376 duplicate records** were identified and removed.

Logical consistency checks were also performed to identify potentially inconsistent candidate information.

Potential outliers were analyzed using the IQR method. Valid extreme values were not automatically removed because they may represent genuine candidate profiles.

---

## 6. Exploratory Data Analysis

EDA was performed to understand candidate characteristics and their relationship with placement outcomes.

The analysis focused on:

- Academic performance vs placement
- Technical score vs placement
- Skills match vs placement
- Experience vs placement
- Company tier vs placement
- Competition level vs placement
- Interview performance
- Certification impact

### Key EDA Insights

**Technical Performance**

Placed candidates generally showed higher technical scores compared with candidates who were not placed.

**Skills Match**

Skills alignment with job requirements was an important candidate characteristic.

**Experience**

Years of experience showed a relationship with placement outcomes and was also important in the Machine Learning model.

**Competition**

Higher competition levels were associated with lower observed placement rates.

**Company Tier**

Placement rates were relatively similar across company tiers, indicating that company tier alone was not a strong differentiating factor.

---

## 7. Feature Engineering

Meaningful features were created from the existing candidate information.

### Experience Category

Candidates were grouped into:

- Fresher
- Junior
- Senior

### Academic Average

SSC, HSC, and Degree percentages were combined to create an overall academic average.

### Academic Band

Candidates were categorized into:

- Low
- Medium
- High

### Skills Match Level

Skills match percentage was categorized into:

- Low
- Medium
- High

### Interview Score

Technical, aptitude, and communication scores were combined to create an overall interview score.

### Interview Performance

Interview scores were categorized into:

- Low
- Medium
- High

---

## 8. Machine Learning

Since the target variable contains two classes, classification algorithms were used.

Six Machine Learning models were trained and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. K-Nearest Neighbors (KNN)
5. Support Vector Machine (SVM)
6. Naive Bayes

The dataset was divided into training and testing sets, and appropriate preprocessing and feature scaling were applied.

---

## 9. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- AUC

These metrics were used together to provide a better understanding of model performance.

### Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 86.03% | 79.23% | 73.01% | 75.99% | 90.37% |
| Decision Tree | 82.62% | 71.27% | 71.37% | 71.32% | 93.16% |
| **Random Forest** | **89.09%** | **86.83%** | **75.39%** | **80.71%** | 79.44% |
| KNN | 73.48% | 56.87% | 51.27% | 53.92% | **95.73%** |
| SVM | 83.27% | 78.24% | 61.98% | 69.17% | 76.82% |
| Naive Bayes | 84.36% | 77.02% | 68.90% | 72.73% | 90.83% |

---

## 10. Best Model

**Random Forest** was selected as the final model because it achieved the strongest overall performance across the main evaluation metrics.

### Random Forest Performance

- **Accuracy:** 89.09%
- **Precision:** 86.83%
- **Recall:** 75.39%
- **F1 Score:** 80.71%

KNN achieved the highest AUC of **95.73%**, but its overall Accuracy, Precision, Recall, and F1 Score were lower than Random Forest.

Therefore, Random Forest was selected as the final model based on overall performance.

---

## 11. Feature Importance

Feature importance analysis was performed using the Random Forest model.

The important features included:

1. Technical Score
2. Years of Experience
3. Skills Match Percentage
4. Expected CTC
5. Communication Score
6. Previous CTC
7. Aptitude Score
8. Job Role Match
9. HSC Percentage
10. Degree Percentage

### Key Insight

Technical score was the most important feature in the model.

This indicates that technical performance, experience, skills alignment, compensation expectations, and communication ability are important factors contributing to placement prediction.

---

## 12. Streamlit Dashboard

A **Streamlit dashboard** was developed to present the project results in an easy-to-understand format.

The dashboard includes seven key performance indicators:

1. **Total Candidates**
2. **Placement Rate (%)**
3. **Job Acceptance Rate (%)**
4. **Average Interview Score**
5. **Average Skills Match %**
6. **Offer Dropout Rate**
7. **High-Risk Candidate Percentage**

### Current Dashboard Results

| KPI | Result |
|---|---:|
| Total Candidates | 51,500 |
| Placement Rate | 30.3% |
| Job Acceptance Rate | 30.3% |
| Average Interview Score | 66.0 |
| Average Skills Match | 73.9% |
| Offer Dropout Rate | N/A |
| High-Risk Candidate Percentage | 0.0% |

### KPI Note

There is no separate job acceptance field in the current dataset, so **Placed candidates are treated as accepted placements** for this project.

A true Offer Dropout Rate cannot be calculated because the dataset does not contain a separate offer-status field.

---

## 13. Key Business Insights

The project identified several important insights:

- Technical performance is strongly associated with placement.
- Skills alignment is an important candidate characteristic.
- Experience contributes to placement prediction.
- Communication skills also contribute to candidate evaluation.
- Higher competition can reduce observed placement rates.
- Company tier alone does not strongly determine placement.
- Multiple candidate characteristics should be considered together rather than relying on a single factor.

---

## 14. Business Value

The project can help HR teams:

- Understand candidate profiles.
- Identify important placement factors.
- Analyze candidate performance.
- Identify potential skill gaps.
- Support candidate screening.
- Make more data-driven recruitment decisions.
- Reduce manual analysis effort.

The prediction model should support HR decisions rather than completely replace human judgment.

---

## 15. Project Story

The project follows a simple business story:

**Business Problem**  
↓  
**Candidate Data**  
↓  
**Data Cleaning**  
↓  
**Candidate Analysis**  
↓  
**Feature Engineering**  
↓  
**Machine Learning**  
↓  
**Model Comparison**  
↓  
**Best Model Selection**  
↓  
**Feature Importance**  
↓  
**Candidate Prediction**  
↓  
**Streamlit Dashboard**  
↓  
**Business Decision Support**

This demonstrates how raw candidate data can be converted into meaningful insights and Machine Learning predictions.

---

## 16. Project Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- MySQL
- Streamlit
- Jupyter Notebook
- VS Code

---

## 17. Project Limitations

- The dataset does not contain a separate offer-status field.
- A true Offer Dropout Rate therefore cannot be calculated.
- Job Acceptance Rate is represented using the placement status.
- The model is based on historical candidate data.
- Model predictions should not be treated as guaranteed outcomes.
- Human HR judgment is still required for final recruitment decisions.

---

## 18. Future Enhancements

Future improvements can include:

- Adding a candidate prediction form to Streamlit.
- Showing placement probability.
- Adding interactive charts and filters.
- Performing hyperparameter tuning.
- Applying cross-validation.
- Adding more detailed offer and acceptance data.
- Improving model performance.
- Deploying the dashboard for real-world HR use.

---

## 19. Conclusion

The **HR Job Placement Prediction** project demonstrates an end-to-end Data Science and Machine Learning workflow for analyzing candidate placement outcomes.

The project includes:

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Data preprocessing
- Machine Learning
- Model comparison
- Feature importance
- Streamlit dashboard
- Business insights

Six classification algorithms were compared, and **Random Forest** was selected as the final model based on its overall performance.

The final Random Forest model achieved:

**89.09% Accuracy**  
**86.83% Precision**  
**75.39% Recall**  
**80.71% F1 Score**

Overall, the project demonstrates how candidate data can be transformed into useful insights and predictive information to support **data-driven HR and recruitment decisions**.

---

## 20. Final Project Summary

> **HR Job Placement Prediction is a Machine Learning classification project that analyzes candidate academic performance, technical skills, interview performance, experience, skills match, and recruitment-related factors to predict placement outcomes. The project includes data cleaning, EDA, feature engineering, Machine Learning, model evaluation, feature importance analysis, and a Streamlit dashboard. Six classification models were compared, and Random Forest was selected as the final model with 89.09% accuracy. The project provides useful business insights that can support HR teams in making data-driven recruitment decisions.**