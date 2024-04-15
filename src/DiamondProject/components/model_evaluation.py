import os,sys
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from urllib.parse import urlparse
from src.DiamondProject.utils.util import load_object
from src.DiamondProject.logger.logging import logging
from src.DiamondProject.exception.exception import customexception
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

class ModelEvaluation:
    def __init__(self):
        logging.info("evaluation started")

    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        logging.info("Evaluation metrics captured")
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_test,y_test,=(test_array[:,:-1],test_array[:,-1])
            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)
            logging.info("model has registered")
            tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type_store)

            with mlflow.start_run():
                prediction=model.predict(X_test)
                (rmse,mae,r2)=self.eval_metrics(y_test ,prediction)
                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)

                if tracking_url_type_store!="file":
                    mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model,"model")

        except Exception as e:
            raise customexception(e,sys)