import os
import sys 
sys.path.append(os.path.abspath('..'))

import sqlite3
from src import config
import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_data():
    """Loads data from the SQLite database."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    query = f"SELECT * FROM {config.RAW_TABLE}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

df=load_data()
# Per far runnare il programma bisogna usare questa linea di codice nel terminal: streamlit run 'nome file'

# linear 
with open(os.path.join(config.MODELS_PATH, "linear.pickle"), "rb") as file:
        clf = pickle.load(file)

st.title("Real Estate Valuation")

# text input 


latitudine = st.number_input("Inserisci la latitudine:")
longitudine = st.number_input("Inserisci la longitudine:")

if st.button("predici costo immobile"):
    if latitudine == 0.0 or longitudine == 0.0:
        st.warning("Per favore inserisci dei valori validi.")
    else: 
        riga_base = df.mean().to_frame().T  # DataFrame con una sola riga
        riga_base = df.drop('Y house price of unit area', axis=1)
        # Modifica solo le due colonne desiderate
        riga_base['X5 latitude'] = latitudine
        riga_base['X6 longitude'] = longitudine

        #    Previsione
        prediction = clf.predict(riga_base)[0]
        st.success(f"il valore stimato è: {prediction.round(2)}")

 