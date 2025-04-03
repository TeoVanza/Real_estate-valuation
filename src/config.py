import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths for raw data (Excel files)
RAW_DATA_PATH = os.path.join(BASE_DIR, "../data/raw/")

# SQLite Database Path
DATABASE_PATH = os.path.join(BASE_DIR, "../database/database.db")

# Raw Data Table Name
RAW_TABLE = "raw_data"

# Logging Configuration
LOGGING_LEVEL = "INFO"

# Saved models 
MODELS_PATH = "../models/"
