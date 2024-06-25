from utils.file import ler_moedas, verificar_criar_excel, salvar_dataframe
from utils import crypto

def main():
    if verificar_criar_excel():
        # Arquivo com as moedas já existe -> executar atualização
        print("Arquivo exchanges.xlsx já existe.")

        lista_moedas = ler_moedas()
        print(lista_moedas)

        df = crypto.att_cryptos(lista_crypto=lista_moedas)
        print(df)

        salvar_dataframe(df)
        
    else:
        # Arquivo criado, solicitar preenchimento
        print("Arquivo exchanges.xlsx criado.")

if __name__ == "__main__":
    main()