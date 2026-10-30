# Machine Learning & Predictive Analytics

## Overview
Machine learning work completed during my M.S. in Business Analytics. This repository demonstrates a practical analytics workflow from data preparation through model evaluation, with an emphasis on applying predictive methods to business-oriented problems.

## Techniques
- Data Preprocessing
- Feature Engineering
- Classification
- Model Evaluation
- Predictive Analytics

## Tools
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Skills Demonstrated
- Machine Learning
- Predictive Analytics
- Data Analysis
- Model Evaluation
- Analytical Problem Solving

## Portfolio Relevance
This repository complements my Data Analyst and Analytics Internship portfolio by showing experience with Python-based predictive modeling and model evaluation.

## Author
**Heenu Kumari**  
M.S. Business Analytics, Santa Clara University  
[LinkedIn](https://www.linkedin.com/in/heenu-kumari-9b062a3b4) | [GitHub](https://github.com/hkumari-a11y)

## Analytical workflow
This repository represents graduate-level practice with predictive analytics. The topics above describe the learning focus; the actual code and notebooks are the source of truth for which algorithms, datasets, and evaluation metrics were used.

## How to review
1. Identify the prediction question and target variable in the project files.
2. Review preprocessing and any train/test split.
3. Inspect model fitting and evaluation code.
4. Interpret metrics only from recorded outputs, not assumed performance.

## Next improvements
- Name the dataset, target, and algorithms used in each included notebook.
- Add verified evaluation metrics and limitations.
- Document environment and steps needed to reproduce results.

## RAFT school revenue modeling — reviewed group results
A graduate group project compared a simple baseline with **log-linear regression (OLS)** and **k-nearest neighbors (KNN)** to predict school revenue. A separate review workbook summarized the group's existing analysis; **no new model was fitted as part of that review**.

- **Evaluation design:** 157 FY23 training schools and 66 FY25 test schools.
- **Test mean absolute error (MAE):** baseline **$299.23**, OLS **$316.13**, KNN **$307.05**.
- **Test median absolute error:** baseline **$88.15**, OLS **$108.09**, KNN **$83.48**.
- **Finding:** the baseline had the lowest overall MAE; KNN had the lowest median absolute error. These metrics reflect the reviewed test split, not guaranteed future performance.

**Attribution and limitations:** This summarizes existing collaborative project results and subsequent review, rather than claiming independent model development. No underlying group dataset or restricted workbook is published here. The source review also notes that test R² was unavailable and reported p-values were approximations from robust t statistics.

## Additional hands-on project
- [Revenue Model Evaluation — Python](projects/revenue-model-evaluation/README.md): MAE, RMSE, and median error comparison using fictional predictions.

- [Model Evaluation Checklist](projects/model-evaluation-checklist/README.md): a practical methodology reference for regression and KNN.
