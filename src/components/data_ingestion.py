import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig
# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer

# Define a configuration class for data ingestion using dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")  # Path to save the training data
    test_data_path: str = os.path.join('artifacts', "test.csv")  # Path to save the test data
    raw_data_path: str = os.path.join('artifacts', "data.csv")  # Path to save the raw data

# Define a class for data ingestion
class DataIngestion:
    def __init__(self):
        # Initialize the data ingestion configuration
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset into a DataFrame
            df = pd.read_csv('notebook\\data\\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Create the directory if it doesn't exist and save the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            # Split the dataset into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training and testing sets as CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Return the paths to the training and testing data files
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Create an instance of the DataIngestion class and initiate data ingestion
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # # Create an instance of the DataTransformation class and initiate data transformation
    # data_transformation = DataTransformation()
    # train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # # Create an instance of the ModelTrainer class and initiate model training
    # modeltrainer = ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
