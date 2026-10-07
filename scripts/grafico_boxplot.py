from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_boxplot.csv")

ordem = df.groupby("departamento")["salario"].median().sort_values().index
dados = [df.loc[df["departamento"] == d, "salario"] for d in ordem]

fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot(dados, tick_labels=ordem, patch_artist=True,
           boxprops={"facecolor": "#9ecae1"}, medianprops={"color": "black"})
ax.set_title("Distribuição salarial por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "boxplot.png", dpi=150)
plt.show()

