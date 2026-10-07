from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_distribuicao.csv")

import seaborn as sns

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["idade"], bins=15, kde=True, color="#4C78A8", ax=ax)
ax.axvline(df["idade"].mean(), color="red", linestyle="--",
           label=f"Média: {df['idade'].mean():.1f}")
ax.axvline(df["idade"].median(), color="green", linestyle=":",
           label=f"Mediana: {df['idade'].median():.1f}")
ax.set_title("Distribuição da idade dos clientes")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend()

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "distribuicao.png", dpi=150)
plt.show()

