from src import config
import sqlite3
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
# Set up logging

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def train_model():
    """train logistic model"""
    df = load_data()
    X=df.drop('Y house price of unit area', axis=1)
    y=df['Y house price of unit area']
    df_indices = df.index

    # Train-test split (preserve indices)
    X_train, X_test, y_train, y_test, train_idx, test_idx = train_test_split(
        X, y, df_indices, test_size=0.2, random_state=42
    )

    clf=LinearRegression()
    clf.fit(X_train, y_train)

    logging.info('saving linear model...')
    with open(os.path.join(config.MODELS_PATH, "linear.pickle"), "wb") as file:
        pickle.dump(clf,file)
