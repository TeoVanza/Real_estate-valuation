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
scelta = st.radio("Scegli la modalità:", ["Semplice", "Avanzata"])

if scelta == "Semplice":
    latitudine = st.number_input("Inserisci la latitudine nella regione di Sindian, Nuova Taipei, Taiwan:", min_value=df['X5 latitude'].min(), max_value=df['X5 latitude'].max(), format="%.5f", step=0.00001)
    longitudine = st.number_input("Inserisci la longitudine nella regione di Sindian, Nuova Taipei, Taiwan:",min_value=df['X6 longitude'].min(), max_value=df['X6 longitude'].max(), format="%.5f", step=0.00001)
elif scelta == "Avanzata":
    eta = st.number_input("inserisci età dell'immobile:", min_value=0, step=1, format="%d")
    stazione = st.number_input("distanza dalla stazione in m:",min_value=0, step=1, format="%d")
    market = st.number_input("n° supermarket nelle vicinanza:",min_value=0, max_value=20, step=1, format="%d")

if st.button("predici costo immobile"):
    if scelta == "Semplice":
        riga_base = df.mean().to_frame().T  # DataFrame con una sola riga
        riga_base = df.drop('Y house price of unit area', axis=1)
        # Modifica solo le due colonne desiderate
        riga_base['X5 latitude'] = latitudine
        riga_base['X6 longitude'] = longitudine
        #    Previsione
        prediction = clf.predict(riga_base)[0]
        euro_m = (prediction*10000)/(3.3*35)
        st.success(f"il valore stimato in euro per metri quadrati è: {euro_m.round(2)}")
    elif scelta == "Avanzata":
        riga_base = df.mean().to_frame().T  # DataFrame con una sola riga
        riga_base = df.drop('Y house price of unit area', axis=1)
        # Modifica solo le 3 colonne desiderate
        riga_base['X2 house age'] = eta
        riga_base['X3 distance to the nearest MRT station'] = stazione
        riga_base['X4 number of convenience stores'] = market

        prediction = clf.predict(riga_base)[0]
        euro_m = (prediction*10000)/(3.3*35)
        st.success(f"il valore stimato in euro per metri quadrati è: {euro_m.round(2)}")


        

 