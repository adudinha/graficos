from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_frequencia.csv")

freq = df["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.bar(freq.index, freq.values, color="#4C78A8")
ax.bar_label(barras, padding=3)
ax.set_title("Frequência de chamados por tipo de atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Quantidade de chamados")

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "frequencia.png", dpi=150)
plt.show()

