# 💵Salary Predictor

A **machine learning application** that predicts salaries based on **job title**, **employment type**, **company size**, and **experience level**. The project covers **data cleaning**, **exploratory data analysis (EDA)**, **Random Forest regression**, **model evaluation**, and a **Streamlit web app** for real-time salary predictions.

## Features

* **Data Cleaning & Preprocessing**

  * Handles missing values and removes inconsistencies.
  * Converts salary values to numeric and encodes categorical features.

* **Exploratory Data Analysis (EDA)**

  * Visualizes salary distributions and trends across job titles.
  * Identifies outliers and patterns for better model accuracy.

* **Machine Learning Model**

  * Random Forest Regressor trained on job-related features.
  * Predicts salaries accurately for different job profiles.

* **Model Evaluation**

  * Measures performance using **MAE**, **MSE**, and **R² score**.
  * Evaluates predictions to ensure reliability and accuracy.

* **Streamlit Web App**

  * Interactive interface to input job details and get real-time salary predictions.
  * User-friendly layout with styled interface for better usability.

## Dataset

* Includes job-related features such as `job_title`, `employment_type`, `company_size`, `salary_in_usd`, and `experience_level`.
* Cleaned and preprocessed to ensure numeric consistency.
* Experience levels randomly assigned if missing.

## Technologies Used

* **Python**
* **Pandas & NumPy** – data processing
* **Scikit-learn** – Random Forest regression
* **Seaborn & Matplotlib** – data visualization
* **Streamlit** – interactive web application
