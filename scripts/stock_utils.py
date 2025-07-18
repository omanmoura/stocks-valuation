import yfinance as yf
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extrair_historico (ticker_list: list, tipo: str):
    lista = pd.DataFrame()
    for ticker in ticker_list:
        logging.info(f'Extraindo informações do(a) {tipo}: {ticker}')
        acao = yf.Ticker(ticker)
        df = pd.DataFrame.from_dict(acao.info, orient='index').T
        df['ticker'] = ticker
        df.set_index('ticker', inplace=True)
        lista = pd.concat([lista, df])
    return lista

def tratar_historico (ativo: list, tipo: str):
    if tipo == "FII":
        ativo = ativo[['dividendYield', 'priceToBook', 'volume', 'bookValue']]
    elif tipo == "ACOES":
        ativo = ativo[['dividendYield', 'priceToBook', 'volume', 'bookValue']]
    elif tipo == "FIINFRA":
        ativo = ativo[['lastDividendValue', 'previousClose', 'currentPrice', 'averageVolume']]
    return ativo

def salvar_historico(ativo: pd.DataFrame, tipo: str):
    if tipo == "FII":
        logging.info('Salvando arquivo CSV em ./data/raw/historico_fiis.csv')
        ativo.to_csv('../data/raw/historico_fiis.csv')
    elif tipo == "ACOES":
        logging.info('Salvando arquivo CSV em .data/raw/historico_acoes.csv')
        ativo.to_csv('../data/raw/historico_acoes.csv')
    elif tipo == "FIINFRA":
        logging.info('Salvando arquivo CSV em ./data/raw/historico_fiinfras.csv')
        ativo.to_csv('../data/raw/historico_fiinfras.csv')