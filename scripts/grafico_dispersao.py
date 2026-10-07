from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 6))
for sexo, grupo in df.groupby("sexo"):
    ax.scatter(grupo["altura_cm"], grupo["peso_kg"], label=sexo, alpha=0.7)
ax.set_title("Relação entre altura e peso")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "dispersao.png", dpi=150)
plt.show()

