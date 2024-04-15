import pandas as pd
import numpy as np
from src.DiamondProject.logger.logging import logging
from src.DiamondProject.exception.exception import customexception
import os,sys
from dataclasses import  dataclass
from pathlib import Path



from src.DiamondProject.utils.util import save_object,evaluate_model

from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config =ModelTrainerConfig()
    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("splitting the into X and Y")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                "LinearRegression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "ElasticNet": ElasticNet()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print("\n================================")
            logging.info(f"Model Report:{model_report}")

            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]
            print(f"Best Model Foun,Model Name:{best_model_name},R2 Score:{best_model_score}")
            logging.info(f"Best Model Found,Model Name:{best_model_name},R2 Score:{best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            raise customexception(e,sys)