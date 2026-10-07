from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_regressao.csv")

import numpy as np
from scipy import stats

res = stats.linregress(df["renda_mensal"], df["gasto_mensal"])
x = np.linspace(df["renda_mensal"].min(), df["renda_mensal"].max(), 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df["renda_mensal"], df["gasto_mensal"], alpha=0.6, label="Observações")
ax.plot(x, res.intercept + res.slope * x, color="red",
        label=f"y = {res.slope:.2f}x + {res.intercept:.2f}  (R² = {res.rvalue**2:.3f})")
ax.set_title("Regressão linear: renda mensal x gasto mensal")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "regressao.png", dpi=150)
plt.show()

