# 🧠 End-to-End Bank Customer Churn Prediction using MLflow, DVC, and Docker

---

## 📍 Introduction

Customer churn refers to the loss of customers by a business. In the banking sector, churn prediction is a vital component of customer relationship management (CRM). By identifying customers who are likely to leave, businesses can take proactive measures such as personalized communication, offers, or incentives to retain them.

This project demonstrates a complete machine learning pipeline for **predicting customer churn**. The pipeline is production-ready and includes data tracking, version control, containerization, CI/CD integration, and deployment via Flask and Docker.

---

## 🔍 Problem Statement

Banks lose a significant amount of revenue due to customer attrition. The goal is to build a machine learning model that classifies whether a customer will **churn or not**, based on historical data (demographics, account activity, transactions, etc.). 

By doing so, the bank can:
- Understand customer behavior
- Increase customer retention
- Reduce operational costs due to attrition
- Implement personalized retention strategies

---

## 🧠 What is MLflow?

[MLflow](https://mlflow.org/) is an open-source platform for managing the end-to-end machine learning lifecycle. It allows:
- **Experiment Tracking**: Log and compare model runs.
- **Project Packaging**: Reproducible code and environment.
- **Model Registry**: Store, annotate, and manage model versions.
- **Deployment**: Serve models with REST APIs or in batch.

In our project, we use MLflow to **track experiments, log metrics**, and **register models**.

---

## 📦 What is DVC?

[Data Version Control (DVC)](https://dvc.org/) is a version control system for data and machine learning pipelines. It helps manage:
- Large datasets and model files
- Reproducible pipelines
- Data provenance and lineage

DVC integrates with Git, and in this project, we use it to:
- Track data and models
- Manage multiple pipeline stages
- Reproduce experiments and results easily

---

## 🧰 Tech Stack

| Category        | Tools Used                                      |
|----------------|--------------------------------------------------|
| Programming     | Python                                          |
| ML Lifecycle    | MLflow                                          |
| Version Control | Git + DVC                                       |
| Pipeline        | Python scripts & YAML                           |
| Model           | scikit-learn, LightGBM, Optuna                  |
| Web Deployment  | Flask                                           |
| Containerization| Docker                                          |
| CI/CD           | GitHub Actions                                  |

---

## 📁 Project Directory Structure

```bash
END-TO-END-CUSTOMER-CHURN-PREDICTION/
│
├── .github/                  # GitHub CI/CD workflows
├── artifacts/                # Saved models, predictions, and intermediate outputs
├── config/                   # config.yaml with settings for each pipeline stage
├── data/                     # Raw and processed data
├── images/                   # Plots and graphs
├── logs/                     # Execution logs
├── research/                 # Jupyter notebooks for each ML stage
├── src/                      # Core Python source code
│   └── mlFlowProject/
│       ├── components/       # Data ingestion, transformation, training, etc.
│       └── __init__.py
├── static/                   # Web static files (CSS, JS)
├── templates/                # HTML templates for the Flask app
├── venv/                     # Python virtual environment (not versioned)
│
├── .dockerignore             # Ignore rules for Docker build context
├── .gitignore                # Ignore rules for Git
├── app.py                    # Flask web application
├── Dockerfile                # Docker configuration file
├── dvc.yaml                  # DVC pipeline stage definitions
├── LICENSE                   # MIT License
├── main.py                   # Main entry script to run the ML pipeline
├── params.yaml               # Model and pipeline parameters
├── README.md                 # This documentation
├── requirements.txt          # Project dependencies
├── schema.yaml               # Data schema definition
├── setup.py                  # Package setup (optional)
├── submission.xlsx           # Sample result submission file
└── template.py               # Utility template
```

# Step-by-Step ML Pipeline Explanation

### 1️⃣ Data Ingestion (`01_data_ingestion.ipynb` / `data_ingestion.py`)
- Reads raw data from a local or remote source.
- Splits data into training and testing sets.
- Saves the datasets in the `artifacts/` folder for reuse and tracking.

---

### 2️⃣ Data Validation (`02_data_validation.ipynb`)
- Validates the schema defined in `schema.yaml`.
- Checks for missing values, data types, and column mismatches.
- Logs any discrepancies in the `logs/` folder.

---

### 3️⃣ Data Transformation (`03_data_transformation.ipynb`)
- Applies encoding techniques (e.g., OneHot Encoding, Label Encoding).
- Normalizes or scales numerical features.
- Saves the processed datasets for model input.

---

### 4️⃣ Model Training (`04_model_trainer.ipynb`)
- Trains one or more machine learning models (e.g., RandomForest, LightGBM).
- Logs parameters, metrics, and models using MLflow.
- Saves the best-performing model as an artifact.

---

### 5️⃣ Model Evaluation (`05_model_evaluation.ipynb`)
- Compares model predictions on the test data.
- Computes performance metrics like accuracy, ROC-AUC, precision, and recall.
- Logs final metrics and selects the best model for deployment.

---

### 🌍 Flask Web Application (`app.py`)
- Provides a simple user interface to upload new customer data.
- Predicts whether the customer will churn.
- Displays prediction results on the web interface.

