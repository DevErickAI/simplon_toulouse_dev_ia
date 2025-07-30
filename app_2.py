# le chiffre d'affaires par produit

import plotly.express as px
import pandas as pd

données = pd.read_csv('ventes.csv')

données['revenue'] = données['prix'] * données['qte']
revenue_par_produit = données.groupby('produit')['revenue'].sum().reset_index()

figure = px.pie(revenue_par_produit, values='revenue', names='produit', title='Chiffre affaires par produit')

# Sauvegarder en fichier HTML
figure.write_html('revenue-par-produit.html')

print('revenue-par-produit.html généré avec succès !')
