from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_barras.csv")

tabela = df.pivot(index="categoria", columns="regiao", values="vendas_medias")

ax = tabela.plot(kind="bar", figsize=(9, 5), width=0.8)
ax.set_title("Vendas médias por categoria e região")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.legend(title="Região")
ax.tick_params(axis="x", rotation=0)
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "barras.png", dpi=150)
plt.show()

