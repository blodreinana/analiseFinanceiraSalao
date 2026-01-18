import pandas as pd
import numpy as np

def limpar_dinheiro(valor):
    if pd.isna(valor) or str(valor).strip() == '':
        return 0.0
    v = str(valor).strip().replace('R$', '').replace(' ', '')
    v = v.replace('.', '').replace(',', '.')
    try:
        return float(v)
    except:
        return 0.0

def executar_etl(caminho_agenda, caminho_distrib, caminho_manut, caminho_lucros):
    print("   [ETL] Iniciando processamento AVANÇADO...")
    
    df_raw = pd.read_csv(caminho_agenda, header=None)
    idx_header = df_raw[df_raw.isin(['Serviços', 'Serviço']).any(axis=1)].index[0]
    
    df_agenda = df_raw[idx_header+1:].copy()
    df_agenda.columns = df_raw.iloc[idx_header].values
    
    cols_map = {c: c.strip() for c in df_agenda.columns}
    df_agenda = df_agenda.rename(columns=cols_map)
    df_agenda.rename(columns={'Preço (R$)': 'Preço'}, inplace=True)
    
    df_agenda['Preço_Num'] = df_agenda['Preço'].apply(limpar_dinheiro)
    
    cols_dias = [c for c in df_agenda.columns if 'feira' in c or 'Sábado' in c]
    df_melt = df_agenda.melt(id_vars=['Serviços', 'Preço_Num'], value_vars=cols_dias, var_name='Dia', value_name='Info')
    df_vendas = df_melt.dropna(subset=['Info']).copy()
    
    
    print("   [ETL] Calculando métricas financeiras cruzadas...")
    
    df_manut = pd.read_csv(caminho_manut, header=None)
    custo_total_manut = 0
    custo_funcionarias_manut = 0
    
    str_manut = df_manut.astype(str)
    for i, row in str_manut.iterrows():
        row_str = " ".join(row.values)
        if "Total Gasto Mensal" in row_str:
            for val in row:
                if "R$" in val: custo_total_manut = limpar_dinheiro(val)
        if "Funcionárias" in row_str:
            for val in row:
                if "R$" in val: custo_funcionarias_manut = limpar_dinheiro(val)

    df_dist = pd.read_csv(caminho_distrib, header=None)
    ganho_proprietaria_servicos = 0
    receita_total = 0
    
    str_dist = df_dist.astype(str)
    for i, row in str_dist.iterrows():
        for j, val in enumerate(row):
            if "Propritária" in val or "Proprietária" in val:
                 try:
                     ganho_proprietaria_servicos = limpar_dinheiro(df_dist.iloc[i+1, j])
                 except: pass
            if "Arrecadação Total" in val:
                 try:
                     receita_total = limpar_dinheiro(df_dist.iloc[i+1, j])
                 except: pass

    custo_operacional = custo_total_manut - custo_funcionarias_manut
    lucro_negocio = receita_total - custo_total_manut
    lucro_final_dona = ganho_proprietaria_servicos + lucro_negocio

    financeiro = {
        "receita_total": receita_total,
        "custo_funcionarias": custo_funcionarias_manut,
        "custo_operacional": custo_operacional,
        "ganho_servicos_dona": ganho_proprietaria_servicos,
        "lucro_negocio_sobra": lucro_negocio,
        "lucro_final_dona": lucro_final_dona
    }
    
    return {"vendas": df_vendas, "financeiro": financeiro}