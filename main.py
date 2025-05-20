import requests
import pandas as pd
from io import StringIO 

url = "https://www.coingecko.com/pt"
page = requests.get(url)

# Usa StringIO para envolver o conteúdo HTML
html_content = StringIO(page.text)

tables = pd.read_html(html_content)

print(f"{len(tables)} tabelas encontradas.")
print(tables[0].head())
