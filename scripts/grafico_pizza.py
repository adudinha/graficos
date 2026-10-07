from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
df = pd.read_csv(RAIZ / "data" / "dados_pizza.csv")

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(df["faturamento"], labels=df["canal_venda"], autopct="%1.1f%%",
       startangle=90, counterclock=False, wedgeprops={"edgecolor": "white"})
ax.set_title("Participação no faturamento por canal de venda")

plt.tight_layout()
plt.savefig(RAIZ / "graficos" / "pizza.png", dpi=150)
plt.show()

