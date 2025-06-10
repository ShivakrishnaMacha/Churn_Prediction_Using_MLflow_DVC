# 🧠 End-to-End Customer Churn Prediction using MLflow, DVC, and Docker

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
### MLflow Experiment Tracking

![Image](https://github.com/user-attachments/assets/3caf839c-239b-483d-b915-f5f7468b33c6)
![Image](https://github.com/user-attachments/assets/c773fe48-00fe-42a8-8ef0-f4915db75660)
![Image](https://github.com/user-attachments/assets/1a1daac5-724b-4696-aa4f-dc63a2f9f3e9)
![Image](https://github.com/user-attachments/assets/834468e3-c4cb-4e69-9485-16afe3124f94)


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

### 🌐 **Flask Web Interface**  



### 🐳 Docker Containerization
Dockerfile:
```bash
FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:$PORT", "app:app"]
```
To build & run locally
```bash
docker build -t churn-predictor .
docker run -p 5000:5000 churn-predictor
```

### 🚀 Heroku Deployment (Live + CI/CD)

<img src="https://github.com/user-attachments/assets/97830778-a98e-4683-b04a-dc582a738e90" alt="Image" width="600"/>

**Live URL:**  
🔗 [https://customer-churn-prediction-ml-082f561f1c3a.herokuapp.com](https://customer-churn-prediction-ml-082f561f1c3a.herokuapp.com)

### 🛠 GitHub Actions for Heroku
.github/workflows/main.yml

```bash
name: Deploy to Heroku

on:
  push:
    branches:
      - main

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Deploy to Heroku via Docker
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: ${{ secrets.HEROKU_APP_NAME }}
          heroku_email: ${{ secrets.EMAIL }}
          usedocker: true
```
🎯 CI/CD kicks in automatically on every main push and deploys the app via Docker to Heroku.

### ✅ Final Results

This project demonstrates a complete and production-ready machine learning workflow:

- ✅ **End-to-End ML Pipeline**  
  Covers ETL (data ingestion, validation, transformation), model training, and evaluation.

- ✅ **Reproducible with MLflow + DVC**  
  Track experiments with MLflow and version data/models using DVC.

- ✅ **Containerized with Docker**  
  The entire application is packaged into a Docker container for consistent deployment.

- ✅ **Deployed on Heroku with GitHub Actions**  
  Continuous deployment enabled via GitHub Actions, pushing Docker images to Heroku.

- ✅ **Live Web UI for Churn Predictions**  
  A user-friendly Flask app allows real-time predictions from uploaded CSV files.

### 🙌 Author

**Shivakrishna Macha**  
🎓 MS in Data Analytics & Visualization _(May 2025)_  
📧 shivakrishnamacha67@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shivakrishnamacha/)  


