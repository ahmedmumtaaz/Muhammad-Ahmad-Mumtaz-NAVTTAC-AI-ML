# Modeling notes and self-check

## Data preparation
- **Missing values:** inspect why values are missing before choosing an imputation strategy.
- **Duplicates:** remove only when duplicate records are genuinely redundant.
- **Encoding:** one-hot encoding is a common starting point for nominal categories.
- **Scaling:** standardization is useful for many models whose optimization depends on feature scale.
- **Data leakage:** split first, fit preprocessing on the training set, and only transform the test set.

## Regression
Regression predicts a continuous target.
- MAE: average absolute prediction error.
- RMSE: gives larger errors more influence.
- R²: compares the model against a mean-prediction baseline; it can be negative.

## Classification
Classification predicts a category.
- Accuracy: proportion of predictions that are correct.
- Precision: among predicted positives, the fraction that are truly positive.
- Recall: among actual positives, the fraction found by the model.
- F1: harmonic mean of precision and recall.
- Confusion matrix: counts correct and incorrect predictions by class.

## Questions to answer in your own words
1. Why do we keep a test set separate from training?
2. What could go wrong if a scaler is fitted on the full dataset?
3. When might recall matter more than precision?
4. Why should a baseline model be evaluated before trying a complex model?
5. What additional checks would you perform before deploying a model?
