import matplotlib.pyplot as plt
import seaborn as sns

def gerar_dashboard(dados, caminho_salvar):
    print("   [VIZ] Gerando Dashboard Executiva...")
    df = dados['vendas']
    fin = dados['financeiro']
    
    sns.set_theme(style="whitegrid")
    
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(2, 3)
    
    
    fig.suptitle(f"Relatório Financeiro & Operacional\nLucro Total da Proprietária: R$ {fin['lucro_final_dona']:,.2f}", 
                 fontsize=24, fontweight='bold', color='#2E7D32')

    ax1 = fig.add_subplot(gs[0, 0])
    
    categorias = ['Receita Total', 'Pgto Funcionárias', 'Manutenção (Luz/Prod)', 'Lucro do Negócio']
    valores = [fin['receita_total'], fin['custo_funcionarias'], fin['custo_operacional'], fin['lucro_negocio_sobra']]
    cores = ['#2196F3', '#FF5252', '#FF9800', '#4CAF50']
    
    sns.barplot(x=categorias, y=valores, ax=ax1, palette=cores)
    ax1.set_title("Fluxo de Caixa (Entradas vs Saídas)", fontweight='bold')
    ax1.set_xticklabels(categorias, rotation=15)
    for i, v in enumerate(valores):
        ax1.text(i, v, f"R$ {v:,.0f}", ha='center', va='bottom', fontweight='bold')

    ax2 = fig.add_subplot(gs[0, 1])
    labels = ['Comissão (Serviços Dela)', 'Lucro do Salão (Sobras)']
    sizes = [fin['ganho_servicos_dona'], fin['lucro_negocio_sobra']]
    colors = ['#9C27B0', '#4CAF50']
    
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=(0.05, 0))
    ax2.set_title(f"Composição do Ganho da Dona\n(Total: R$ {fin['lucro_final_dona']:,.2f})", fontweight='bold')

    ax3 = fig.add_subplot(gs[1, :])
    top_servicos = df.groupby('Serviços')['Preço_Num'].sum().sort_values(ascending=False).head(8)
    
    sns.barplot(x=top_servicos.values, y=top_servicos.index, ax=ax3, palette="viridis")
    ax3.set_title("Top Serviços Geradores de Receita", fontweight='bold')
    ax3.set_xlabel("Faturamento (R$)")
    
    ax4 = fig.add_subplot(gs[0, 2])
    ax4.axis('off')
    texto = f"""
    RESUMO EXECUTIVO
    ----------------
    (+) Receita Total:      R$ {fin['receita_total']:,.2f}
    
    (-) Funcionárias:       R$ {fin['custo_funcionarias']:,.2f}
    (-) Custo Operacional:  R$ {fin['custo_operacional']:,.2f}
        (Luz, Água, Produtos)
    
    (=) Lucro Líquido Salão: R$ {fin['lucro_negocio_sobra']:,.2f}
    
    ----------------
    PROPRIETÁRIA:
    (+) Ganho por Serviço:  R$ {fin['ganho_servicos_dona']:,.2f}
    (+) Lucro do Salão:     R$ {fin['lucro_negocio_sobra']:,.2f}
    
    (=) TOTAL NO BOLSO:     R$ {fin['lucro_final_dona']:,.2f}
    """
    ax4.text(0.05, 0.5, texto, family='monospace', fontsize=11, va='center', bbox=dict(boxstyle="round", fc="#E8F5E9"))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(caminho_salvar)
    print(f"   [VIZ] Dashboard salva: {caminho_salvar}")