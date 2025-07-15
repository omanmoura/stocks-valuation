import yfinance as yf
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

TICKERS_ACOES = ['KEPL3.SA', 'KLBN11.SA', 'SLCE3.SA', 'BBAS3.SA', 'ABCB4.SA', 'BBDC4.SA', 'SAPR11.SA', 'TASA4.SA', 'BMGB4.SA']
TICKERS_FIIS = ['BTCI11.SA', 'BTHF11.SA', 'PORD11.SA', 'RVBI11.SA', 'RBFF11.SA', 'VISC11.SA', 'XPML11.SA', 'PVBI11.SA', 'KFOF11.SA', 'BRCR11.SA', 'VILG11.SA', 'CPTS11.SA', 'MCRE11.SA', 'LVBI11.SA', 'JSRE11.SA', 'RBVA11.SA', 'PATL11.SA']
TICKERS_FIINFRAS = ['JURO11.SA', 'KDIF11.SA', 'IFRA11.SA']

acoes = pd.DataFrame()
fiis = pd.DataFrame()
fiinfras = pd.DataFrame()

for ticker in TICKERS_FIIS:
    logging.info(f'Extraindo informações do FII: {ticker}')
    fii = yf.Ticker(ticker)
    df = pd.DataFrame.from_dict(fii.info, orient='index').T
    df['ticker'] = ticker
    df.set_index('ticker', inplace=True)
    fiis = pd.concat([fiis, df])

for ticker in TICKERS_ACOES:
    logging.info(f'Extraindo informações da Ação: {ticker}')
    acao = yf.Ticker(ticker)
    df = pd.DataFrame.from_dict(acao.info, orient='index').T
    df['ticker'] = ticker
    df.set_index('ticker', inplace=True)
    acoes = pd.concat([acoes, df])

for ticker in TICKERS_FIINFRAS:
    logging.info(f'Extraindo informações do FI-Infra: {ticker}')
    fiinfra = yf.Ticker(ticker)
    df = pd.DataFrame.from_dict(fiinfra.info, orient='index').T
    df['ticker'] = ticker
    df.set_index('ticker', inplace=True)
    fiinfras = pd.concat([fiinfras, df])

logging.info('Selecionando as colunas desejadas...')

fiis = fiis[['dividendYield', 'priceToBook', 'volume', 'bookValue']]
acoes = acoes[['dividendYield', 'priceToBook', 'volume', 'bookValue']]
fiinfras = fiinfras[['lastDividendValue', 'previousClose', 'currentPrice', 'averageVolume']]

logging.info('Salvando arquivo CSV em .data/raw/historico_acoes.csv')
acoes.to_csv('../data/raw/historico_acoes.csv')
logging.info('Salvando arquivo CSV em ./data/raw/historico_fiis.csv')
fiis.to_csv('../data/raw/historico_fiis.csv')
logging.info('Salvando arquivo CSV em ./data/raw/historico_fiinfras.csv')
fiinfras.to_csv('../data/raw/historico_fiinfras.csv')
