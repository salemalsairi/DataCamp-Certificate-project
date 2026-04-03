# Real Estate Price Prediction & Data Pipeline

## Overview
This project demonstrates an end-to-end machine learning pipeline, from raw data cleaning to building a highly accurate predictive model for real estate prices.

*Note: To respect proprietary rights, the original dataset is not included. However, I have provided a data generation script (`data.py`) that creates synthetic data with the exact same inconsistencies, missing values, and structure as the real-world dataset I worked on.*

## How to Run This Project
1. Run `python data.py` to generate the synthetic datasets (`house_sales.csv`, `train.csv`, `validation.csv`).
2. Run the main Jupyter Notebook/Python script to see the data cleaning process and model training.

## Technical Highlights
- **Advanced Data Cleaning:** Handled hidden missing values (e.g., extracted '--' as nulls), standardized messy categorical strings (e.g., 'Det.' to 'Detached'), and safely converted string-embedded numbers.
- **Feature Engineering:** Implemented One-Hot Encoding (`pd.get_dummies`) to prepare categorical variables for machine learning.
- **Modeling:** Built a baseline `LinearRegression` model and an optimized `RandomForestRegressor`, successfully reducing the Root Mean Squared Error (RMSE) below the target threshold.

## Technologies Used
- Python, Pandas, Scikit-Learn, NumPy
