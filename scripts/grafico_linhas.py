from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_linhas.csv")

df["data"] = pd.to_datetime(df["data"])
df = df.sort_values("data")
df["media_movel_7d"] = df["vendas"].rolling(7).mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["data"], df["vendas"], color="lightgray", zorder=1)
for loja, grupo in df.groupby("loja"):
    ax.scatter(grupo["data"], grupo["vendas"], s=18, label=loja, zorder=2)
ax.plot(df["data"], df["media_movel_7d"], color="black", linewidth=2,
        label="Média móvel (7 dias)", zorder=3)
ax.set_title("Evolução diária das vendas")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.legend()
ax.grid(alpha=0.3)
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "linhas.png", dpi=150)
plt.show()

