# Dataset

il dataset è dato dalla valutazione degli immobili nel distretto di Sindian, New Taipei City, Taiwan.
la variabile target è il prezzo al metro quadro, però nel dataset i prezzi sono espressi in 10.000 Nuovi Dollari Taiwanesi per Ping, un'unità locale pari a 3,3 metri quadrati. perciò tramite la formula:

$$
\text{Prezzo in €/m²} = \frac{\text{Prezzo in NTD/Ping * 10000}}{3.3 \times \text{Tasso di cambio}}
$$

li ho resi in prezzo al metro quadro per essere piu chiaro 

# modello 

ho usato un modello lineare per fare la predizione 

# Tableu 

il link sotto è per la mappa interattiva del distretto di Sindian, New Taipei City, Taiwan con il prezzo al metro quadro delle case 

https://public.tableau.com/app/profile/matteo.vanzanelli/viz/mappacasetaipeiSindianDist_/Foglio1?publish=yes

# Per UI 

nel terminale bisogna entrare nelle cartella scripts con "cd scripts"
dopodiche si usa il comando "streamlit run UI.py" 
