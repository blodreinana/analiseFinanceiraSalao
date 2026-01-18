# 📊 Análise de Dados & Dashboard Financeiro  
### Salão de Beleza — Projeto de Ciência de Dados

> Projeto Extensionista — CST em Ciência de Dados | UNINTER  
> Desenvolvido de forma **100% autônoma**, do levantamento à análise final.

---

## 🧠 Contexto do Projeto
Este projeto foi desenvolvido ao longo de **1 mês e meio**, de forma **independente**, sem auxílio de IA ou consultorias externas, como parte da Atividade Extensionista do curso de Ciência de Dados.

O trabalho teve como foco aplicar **Inteligência de Negócios** e **Inclusão Digital** em um pequeno negócio real: um **salão de beleza localizado no Brás/SP**, que até então operava apenas com **anotações manuais e planilhas desorganizadas**.

---

## 🎯 Objetivo
Transformar dados financeiros brutos e descentralizados em **informação estratégica**, por meio de um pipeline de dados e uma **Dashboard Executiva**, permitindo que a proprietária visualize de forma clara:

- 📈 Faturamento real x custos operacionais  
- 💰 Lucro líquido mensal  
- ⭐ Serviços mais rentáveis (Curva ABC)  
- 👥 Fluxo de clientes ao longo da semana  

---

## 🔍 Etapas do Desenvolvimento
O projeto contemplou todas as fases de um processo real de dados:

1. **Coleta manual dos dados** diretamente com o negócio  
2. **Estruturação e padronização** das informações  
3. **ETL completo** (extração, limpeza e transformação)  
4. **Análise exploratória**  
5. **Visualização e geração da dashboard final**  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+**
- **Pandas** — ETL e tratamento de dados
- **Matplotlib & Seaborn** — Visualização de dados
- **Git & GitHub** — Versionamento e documentação

---

## 📂 Estrutura do Projeto
O projeto segue uma organização inspirada em arquiteturas profissionais de dados:

```
├── data/
│   ├── raw/          # Dados brutos (ignorado no Git por privacidade)
│   └── processed/   # Dados tratados
│
├── src/
│   ├── etl.py        # Pipeline de limpeza e transformação
│   └── visualizacao.py  # Geração dos gráficos
│
├── output/
│   └── dashboards/  # Imagens das visualizações finais
│
├── main.py           # Arquivo principal de execução
└── requirements.txt
```

> ⚠️ Os dados reais não estão disponíveis no repositório por questões de privacidade do negócio.

---

## 🚀 Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Adicione os arquivos CSV na pasta:
   ```
   data/raw/
   ```

4. Execute o pipeline:
   ```bash
   python main.py
   ```

---

## 📈 Resultados Alcançados
A dashboard gerada proporcionou **clareza financeira imediata** ao negócio, permitindo identificar padrões de faturamento, serviços mais lucrativos e períodos de maior fluxo de clientes.

> Exemplo de insight obtido:  
> **Serviços de alto valor agregado representavam a maior parcela do lucro, apesar de menor volume de atendimentos.**

Essas informações possibilitam **tomada de decisão estratégica**, precificação mais assertiva e melhor planejamento financeiro.

---

## ✨ Aprendizados
- Aplicação prática de ETL em um cenário real  
- Tradução de dados brutos em insights de negócio  
- Desenvolvimento de um projeto do zero, do levantamento à entrega final  
- Comunicação de dados para público não técnico  

---

## 👩‍💻 Desenvolvido por
**Allana Helena Campos Albino**  
Estudante de Ciência de Dados & Engenharia  
Projeto acadêmico com aplicação real de negócio
