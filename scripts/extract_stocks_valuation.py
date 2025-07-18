import logging

from stock_utils import extrair_historico, tratar_historico, salvar_historico

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    TICKERS_ACOES = ['KEPL3.SA', 'KLBN11.SA', 'SLCE3.SA', 'BBAS3.SA', 'ABCB4.SA', 'BBDC4.SA', 'SAPR11.SA', 'TASA4.SA', 'BMGB4.SA']
    TICKERS_FIIS = ['BTCI11.SA', 'BTHF11.SA', 'PORD11.SA', 'RVBI11.SA', 'RBFF11.SA', 'VISC11.SA', 'XPML11.SA', 'PVBI11.SA', 'KFOF11.SA', 'BRCR11.SA', 'VILG11.SA', 'CPTS11.SA', 'MCRE11.SA', 'LVBI11.SA', 'JSRE11.SA', 'RBVA11.SA', 'PATL11.SA']
    TICKERS_FIINFRAS = ['JURO11.SA', 'KDIF11.SA', 'IFRA11.SA']

    # Extraindo histórico dos últimos 30 dias dos ativos
    fiis = extrair_historico(TICKERS_FIIS, "FII")
    acoes = extrair_historico(TICKERS_ACOES, "Ação")
    fiinfras = extrair_historico(TICKERS_FIINFRAS, "FI-Infra")

    # Selecionando colunas desejadas
    logging.info('Selecionando as colunas desejadas...')
    fiis_tratados = tratar_historico(fiis, "FII")
    acoes_tratadas = tratar_historico(acoes, "ACOES")
    fiinfras_tratadas = tratar_historico(fiinfras, "FIINFRA")

    # Salvando os arquivos no diretório de destino
    salvar_historico(fiis_tratados, "FII")
    salvar_historico(acoes_tratadas, "ACOES")
    salvar_historico(fiinfras_tratadas, "FIINFRA")

if __name__ == "__main__":
    main()