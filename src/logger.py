import logging
import os
from datetime import datetime

# Generate a log file name based on the current date and time, replacing ':' with '_'
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create the logs directory path
logs_path = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Set the log file path
    format='%(asctime)s - %(levelname)s: %(message)s',  # Define the log message format
    level=logging.INFO  # Set the logging level to INFO
)


