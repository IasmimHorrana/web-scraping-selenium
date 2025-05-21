import requests
import pandas as pd
from io import StringIO
from time import sleep

def coleta_dados():
    url = "https://www.coingecko.com/pt"

    dados_coletados = []

    for pagina in range(1, 59):
        params = {'items': 300,'page': pagina}

        resposta = requests.get(url, params=params)
        if resposta.status_code != 200:
            print(f"Falha ao acessar página {pagina}, status: {resposta.status_code}")
            continue

        tabelas = pd.read_html(StringIO(resposta.text), skiprows=1)
        print(f"{len(tabelas)} tabelas encontradas na página {pagina}.")

        if tabelas:
            dados_coletados.append(tabelas[0])

        sleep(1)

    # Junta todos os dados coletados em um único DataFrame
    df_final = pd.concat(dados_coletados, ignore_index=True)

    # Ajusta os nomes das colunas para um padrão legível
    df_final.columns = ['Favorito', 'id', 'Moeda', 'Comprar', 'Preço', '1h', '24h', '7d', '30d', 'Volume 24h', 'Capitalização de Mercado', 'FDV', 'Cap/FDV', 'Grafico_7dias']

    # Limpeza dos dados
    df_final = df_final.drop(columns=['Favorito', 'Comprar', 'Grafico_7dias']) #Remove colunas que não vou usar.
    df_final = df_final.drop_duplicates() #Remove linhas duplicadas
    df_final = df_final.dropna(how='all') #Remove linhas vazias
    df_final = df_final.reset_index(drop=True) #Reset index após limpeza

    print(f"Tabelas unificadas e limpas. Total de linhas: {len(df_final)}")

    return df_final

if __name__ == "__main__":
    df = coleta_dados()
    print(df.head())
