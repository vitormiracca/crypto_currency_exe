from datetime import datetime
import ccxt
import pandas as pd

def obter_cotacao_crypto(symbol):
    exchange = ccxt.binance()
    crypto, exchange_symbol = symbol.split('/')

    try:
        ticker = exchange.fetch_ticker(symbol)
        cotacao = round(ticker['close'],2)
        mensagem_erro = None
    
    except ccxt.NetworkError as e:
        cotacao = None
        mensagem_erro = f'NetworkError: {e}'
    except ccxt.ExchangeError as e:
        cotacao = None
        mensagem_erro = f'ExchangeError: {e}'
    except Exception as e:
        cotacao = None
        mensagem_erro = f'Exception: {e}'

    return {
        'crypto': crypto,
        'exchange': exchange_symbol,
        'price': cotacao,
        'update_date': datetime.now(),
        'error': mensagem_erro
    }

def att_cryptos(lista_crypto:list):
    registros = []
    for a in lista_crypto:
        att = obter_cotacao_crypto(a)
        registros.append(att)

    df_cryptos = pd.DataFrame(registros)
    return df_cryptos