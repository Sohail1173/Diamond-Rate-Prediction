import os,sys
from src.DiamondProject.exception.exception import customexception
from src.DiamondProject.logger.logging import logging
from src.DiamondProject.components.data_ingestion import DataIngestion
from src.DiamondProject.components.data_transformation import DataTransformation


# class TrainingPipeline:
#     def __init__(self):
#         self.data_ingestion=DataIngestion()
#         self.data_transformation=DataTransformation()


#     def start_data_ingestion(self):

#         logging.info("entered data_ingestion pipeline")
#         try:
#             data_ingestion=DataIngestion(
#                 data_ingestion_config=self.data_ingestion

#             )

#             data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            
#             logging.info("exited data_ingestion pipeline")
#             return data_ingestion_artifact
            
        
#         except Exception as e:
#             raise customexception(e,sys)

#     def start_data_transformation(self):

#         logging.info("entered data_transformation pipeline")
#         try:
#             data_transformation=DataTransformation(
#                 data_ingestion_artifact=dat
#                 data_transformation_config=self.data_transformation)
            
#         except Exception as e:
#             raise customexception(e,sys)


def training_pipeline():

    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    
