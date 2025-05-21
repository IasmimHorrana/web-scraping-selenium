import requests #para fazer requisições HTTP e acessar páginas web.
import pandas as pd 
from io import StringIO #simula um arquivo em memória com o conteúdo do HTML, necessário para o read_html.
from time import sleep

# URL base do CoinGecko
url = "https://www.coingecko.com/pt"

# Lista para armazenar os dados de todas as páginas
dados_coletados = []

# Loop pelas 58 páginas
for pagina in range(1, 59):
    params = {
        'items': 300,
        'page': pagina
    }

    # Requisição da página com os parâmetros
    resposta = requests.get(url, params=params)

    # Lê o HTML com StringIO
    html_content = StringIO(resposta.text) #simula um arquivo de texto com o HTML.
    tabelas = pd.read_html(html_content, skiprows=1) # procura e extrai tabelas do HTML / skip: pula a primeira linha (que não é parte dos dados).

    print(f"{len(tabelas)} tabelas encontradas na página {pagina}.") #Útil para debug. Vai mostrar se o site respondeu certo.

    if tabelas: # Verifica se há tabelas na resposta
        dados_coletados.append(tabelas[0])

    sleep(1)  # para evitar bloqueio

# Junta todos os DataFrames em um só
df_final = pd.concat(dados_coletados, ignore_index=True)

df_final.columns = ['Favorito', 'id', 'Moeda', 'Comprar', 'Preço', '1h', '24h', '7d', '30d', 'Volume 24h', 'Capitalização de Mercado', 'FDV', 'Cap/FDV', 'Grafico_7dias']

# Exibe as primeiras linhas
print(df_final.head())
