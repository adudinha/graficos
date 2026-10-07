# Visualização de dados: um gráfico por arquivo CSV

Cada script em `scripts/` lê um CSV de `data/` e salva o gráfico em `graficos/`.

| Script | Dados | Gráfico |
|---|---|---|
| `grafico_frequencia.py` | `dados_frequencia.csv` | Barras de frequência por tipo de atendimento |
| `grafico_pizza.py` | `dados_pizza.csv` | Pizza do faturamento por canal de venda |
| `grafico_boxplot.py` | `dados_boxplot.csv` | Boxplot de salário por departamento |
| `grafico_heatmap.py` | `dados_heatmap.csv` | Mapa de calor dia da semana x horário |
| `grafico_dispersao.py` | `dados_dispersao.csv` | Dispersão altura x peso, por sexo |
| `grafico_regressao.py` | `dados_regressao.csv` | Dispersão com reta de regressão (renda x gasto) |
| `grafico_barras.py` | `dados_barras.csv` | Barras agrupadas por categoria e região |
| `grafico_linhas.py` | `dados_linhas.csv` | Série temporal de vendas com média móvel de 7 dias |
| `grafico_distribuicao.py` | `dados_distribuicao.csv` | Histograma com KDE da idade |

## Como executar

```bash
pip install -r requirements.txt
python scripts/grafico_pizza.py   # exemplo; rode qualquer script
```
