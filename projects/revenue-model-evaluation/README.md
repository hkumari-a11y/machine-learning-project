# Regression Model Evaluation: Baseline vs OLS vs KNN

**Status:** Reproducible metric-comparison exercise using synthetic observations.

## Academic connection
In RAFT school revenue modeling coursework, our group compared baseline, OLS and KNN methods. This standalone example demonstrates how to calculate evaluation metrics and compare predictions; it does not reproduce the group's confidential data or original fitted models.

## Questions
- How do MAE, RMSE and median absolute error differ?
- Why might one model have the best overall MAE but another have a better median error?
- Why should a simple baseline always be included?

## Run
`python evaluate_predictions.py`

No external packages required. The fictional numbers are not the actual RAFT predictions.

## Limitations
This script compares already-supplied predictions; it **does not train** an OLS or KNN model and does not estimate p-values or R².
