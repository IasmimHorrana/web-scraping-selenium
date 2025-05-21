from main2_coleta_limpeza import coleta_dados

def salvar_csv():
    df = coleta_dados()
    df.to_csv("dados_criptos.csv", index=False)
    print("CSV exportado com sucesso para 'dados_criptos.csv'.")

if __name__ == "__main__":
    salvar_csv()

