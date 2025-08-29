import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

# Ensure the 'Logs' directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logging Configuration
logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = loggin.StreamLandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)