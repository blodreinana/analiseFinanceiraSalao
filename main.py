from src.etl import executar_etl
from src.visualizacao import gerar_dashboard
import os

FILE_AGENDA = 'data/raw/Planilha Salão - Agendamentos (1).csv'
FILE_DISTRIB = 'data/raw/Planilha Salão - Distribuição.csv'
FILE_MANUT = 'data/raw/Planilha Salão - Manutenção (1).csv'
FILE_LUCROS = 'data/raw/Planilha Salão - Lucros (1).csv'

OUTPUT = 'output/dashboard_financeira_v2.png'

def main():
    os.makedirs('output', exist_ok=True)
    
    dados = executar_etl(FILE_AGENDA, FILE_DISTRIB, FILE_MANUT, FILE_LUCROS)
    gerar_dashboard(dados, OUTPUT)

if __name__ == "__main__":
    main()