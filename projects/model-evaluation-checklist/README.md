# Model Evaluation Checklist for Business Analysts

A practical, reusable checklist based on topics studied in graduate analytics coursework.

## Before fitting
- Define the prediction target, time horizon, and unit of analysis.
- Check missing values, duplicates, and possible data leakage.
- Choose a baseline that would be realistic in production.
- Split training and testing data in a way that respects time and groups.

## For regression
- Report MAE, RMSE, and median absolute error with units.
- Check performance against the baseline.
- Examine residual patterns and performance across relevant groups.
- Explain why large errors matter to the business decision.

## For OLS
- Interpret coefficients with appropriate caveats.
- Review collinearity, functional form, and model assumptions.
- Report p-values and uncertainty only from actual model output.
- Do not infer causality from observational correlations alone.

## For KNN
- Scale numeric predictors without using test data.
- Choose k with validation rather than the test set.
- Consider missingness, irrelevant features, and distance choice.

## Reporting
Present dataset scope, model version, evaluation split, metrics, limitations, and recommended next steps. This document is a methodology guide, not a claim of a completed model.
