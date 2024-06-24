import sys # provide access to system specific parameters and command
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    """
    Extracts and formats detailed information about an exception.
    
    Args:
    error (Exception): The error/exception that occurred.
    error_detail (sys): The sys module to fetch system-specific information.
    
    Returns:
    str: Formatted error message with script name, line number, and error message.
    """
    # Extract exception traceback information
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format the error message with the filename, line number, and error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
    return error_message.format(file_name, exc_tb.tb_lineno, str(error))

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom exception class to provide detailed error messages.
        
        Args:
        error_message (str): The custom error message.
        error_detail (sys): The sys module to fetch system-specific information.
        """
        # Initialize the base class with the error message
        super().__init__(error_message)
        # Store the detailed error message using the helper function
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        """
        Returns the detailed error message when the exception is printed.
        
        Returns:
        str: The detailed error message.
        """
        return self.error_message
if __name__=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("divide by zero")
        raise CustomException(e,sys)
