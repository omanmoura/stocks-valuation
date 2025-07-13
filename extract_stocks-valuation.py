import yfinance as yf
import pandas as pd

TICKERS_ACOES = ['KEPL3.SA', 'KLBN11.SA', 'SLCE3.SA', 'BBAS3.SA', 'ABCB4.SA', 'BBDC4.SA', 'SAPR11.SA', 'TASA4.SA', 'BMGB4.SA']
TICKERS_FIIS = ['BTCI11.SA', 'BTHF11.SA', 'PORD11.SA', 'RVBI11.SA', 'RBFF11.SA', 'VISC11.SA', 'XPML11.SA', 'PVBI11.SA', 'KFOF11.SA', 'BRCR11.SA', 'VILG11.SA', 'CPTS11.SA', 'MCRE11.SA', 'LVBI11.SA', 'JSRE11.SA', 'RBVA11.SA', 'PATL11.SA']
TICKERS_FIINFRAS = ['JURO11.SA', 'KDIF11.SA', 'IFRA11.SA']

acoes = yf.Tickers(' '.join(TICKERS_ACOES))
fiis = yf.Tickers(' '.join(TICKERS_FIIS))
fiinfras = yf.Tickers(' '.join(TICKERS_FIINFRAS))

historico_acoes = acoes.history(period='1mo')
historico_fiis = fiis.history(period='1mo')
historico_fiinfras = fiinfras.history(period='1mo')

historico_acoes.to_csv('./data/raw/historico_acoes.csv')
historico_fiis.to_csv('./data/raw/historico_fiis.csv')
historico_fiinfras.to_csv('./data/raw/historico_fiinfras.csv')
