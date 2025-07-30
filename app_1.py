# les ventes par produit
import pandas as pd
import plotly.express as px

données = pd.read_csv('ventes.csv')
ventes_par_produit = données.groupby('produit')['qte'].sum().reset_index()

figure = px.pie(ventes_par_produit, values='qte', names='produit', title='Les ventes par produit (quantités)')

figure.write_html('ventes-par-produit.html')

print('ventes-par-produit.html généré avec succès !')