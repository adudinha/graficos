from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_heatmap.csv")

import seaborn as sns

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
tabela = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes").loc[dias]

fig, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(tabela, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5,
            cbar_kws={"label": "Movimento de clientes"}, ax=ax)
ax.set_title("Movimento de clientes por dia da semana e horário")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "heatmap.png", dpi=150)
plt.show()

