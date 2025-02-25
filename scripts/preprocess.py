import pandas as pd
import gdown
import os
import logging

class DataPreprocessor:
    def __init__(self, file_path: str, output_dir: str = '../data/', output_file: str = 'data.csv', logger: logging.Logger = None):
        """
        Initialize the DataPreprocessor class with either a Google Drive link or a local file path.

        Parameters:
        file_path (str): The Google Drive shareable link or the local file path to the data file.
        output_dir (str): The directory where the data file will be saved.
        output_file (str): The local file name to save the downloaded data.
        logger (logging.Logger): Logger for tracking events and errors.
        """
        self.file_path = file_path
        self.output_dir = output_dir
        self.output_file = output_file
        self.logger = logger if logger else logging.getLogger(__name__)
