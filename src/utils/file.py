import os
import pandas as pd
    
def verificar_criar_excel(nome_arquivo='exchange.xlsx'):
    """
    Verifica se o arquivo Excel existe. Se não existir, cria um novo arquivo com as colunas 'Crypto' e 'Exchange'
    e uma linha de instrução.
    
    Args:
    nome_arquivo (str): O nome do arquivo Excel a ser verificado/criado. Padrão é 'exchanges.xlsx'.
    
    Returns:
    bool: True se o arquivo já existia, False se foi criado.
    """
    if not os.path.exists(nome_arquivo):
        df = pd.DataFrame(columns=['Crypto', 'Exchange'])
        df.loc[0] = ["Preencha nessa coluna o ticker da moeda digital, ex: BTC", "Preencha o ticker da moeda de comparação, ex: USDT"]
        df.to_excel(nome_arquivo, index=False)
        return False
    return True


def ler_moedas(nome_arquivo='exchange.xlsx'):
    """
    Lê o arquivo Excel e retorna uma lista concatenando os valores das colunas 'Crypto' e 'Exchange'.
    
    Args:
    nome_arquivo (str): O nome do arquivo Excel a ser lido. Padrão é 'exchanges.xlsx'.
    
    Returns:
    list: Uma lista de strings concatenando os valores das colunas 'Crypto' e 'Exchange' no formato 'Crypto/Exchange'.
    """
    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError("O arquivo 'exchange.xlsx' não foi encontrado.")

    df = pd.read_excel(nome_arquivo)
    lista_moedas = [f"{row['Crypto']}/{row['Exchange']}" for index, row in df.iterrows()]
    return lista_moedas

def salvar_dataframe(df, nome_arquivo='exchange.xlsx'):
    """
    Recebe dataframe atualizado e grava em exchange.xlsx.
    
    Args:
    df (DataFrame): O dataframe com as cotações atualizadas.
    nome_arquivo (str): O nome do arquivo Excel a ser gravado. Padrão é 'exchanges.xlsx' (para atualizar sempre no mesmo arquivo que será lido na próxima execução).
    """
    try:
        df.to_excel(nome_arquivo, index=False)
        print(f"DataFrame salvo com sucesso em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar DataFrame: {e}")