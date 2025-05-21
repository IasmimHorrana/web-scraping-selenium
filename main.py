# Rodar só a página 1 para testar
import requests
import pandas as pd
from io import StringIO

url = "https://www.coingecko.com/pt"
params = {'items': 300, 'page': 1}
resposta = requests.get(url, params=params)

tabelas = pd.read_html(StringIO(resposta.text), skiprows=1)
print(f"Tabelas encontradas: {len(tabelas)}")

if tabelas:
    df_teste = tabelas[0]
    df_teste.columns = ['Favorito', 'id', 'Moeda', 'Comprar', 'Preço', '1h', '24h', '7d', '30d',
                        'Volume 24h', 'Capitalização de Mercado', 'FDV', 'Cap/FDV', 'Grafico_7dias']
    
    # Remover duplicatas baseando no 'id' da moeda
    df_teste = df_teste.drop_duplicates(subset=['id'])
    
    # Remover colunas irrelevantes
    df_teste = df_teste.drop(columns=['Favorito', 'Comprar', 'Grafico_7dias'])
    
    print(df_teste.head(10))
    print(f"\nTotal de linhas após limpeza: {len(df_teste)}")
else:
    print("Nenhuma tabela foi encontrada na página.")
