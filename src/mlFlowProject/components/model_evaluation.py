from pathlib import Path
import os
from urllib.parse import urlparse

import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Set environment variables BEFORE importing mlflow
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/shivakrishnamacha67/Churn_Prediction_Using_MLflow_DVC.mlflow"
os.environ["MLFLOW_TRACKING_TOKEN"] = "d92bd692f786b75a761f1b7b154ad757d53b23d3"

# Init tracking BEFORE calling any MLflow run
import mlflow
import mlflow.sklearn
import dagshub

dagshub.init(repo_owner='shivakrishnamacha67', repo_name='Churn_Prediction_Using_MLflow_DVC', mlflow=True)
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("Churn_Prediction_Using_MLflow_DVC")

from mlFlowProject.entity.config_entity import ModelEvaluationConfig
from mlFlowProject.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        actual = np.array(actual).ravel()
        pred = np.array(pred).ravel()

        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred, zero_division=0)
        recall = recall_score(actual, pred, zero_division=0)
        f1 = f1_score(actual, pred, zero_division=0)

        return accuracy, precision, recall, f1

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[self.config.target_column]

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predictions = model.predict(test_x)
            accuracy, precision, recall, f1 = self.eval_metrics(test_y, predictions)

            scores = {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1": f1
            }
            save_json(path=Path(self.config.metric_file_name), data=scores)

            if hasattr(self.config, 'all_params') and self.config.all_params:
                mlflow.log_params(self.config.all_params)

            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1-score", f1)

            # Log the model
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    registered_model_name="LightGBM"
                )
            else:
                mlflow.sklearn.log_model(sk_model=model, artifact_path="model")
