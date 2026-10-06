import pandas as pd

# ==========================================
# ETAPA 1 — CARREGAR OS DADOS
# ==========================================

df = pd.read_csv("data.csv")


# ==========================================
# ETAPA 2 — CONHECER OS DADOS
# ==========================================

print("===== CONHECENDO OS DADOS =====")

print("Quantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))

print("\nNome das colunas:")
print(list(df.columns))

print("\nValores ausentes em cada coluna:")
print(df.isna().sum())


# ==========================================
# ETAPA 3 — ANALISAR O PROBLEMA
# ==========================================

print("\n===== ANÁLISE DO PROBLEMA =====")

print("Colunas com valores ausentes:")

for coluna in df.columns:
    quantidade = df[coluna].isna().sum()

    if quantidade > 0:
        print(coluna, "->", quantidade, "valores ausentes")


# ==========================================
# ETAPA 4 — TOMAR UMA DECISÃO
# ==========================================

print("\n===== LIMPEZA DOS DADOS =====")

# Escolhemos preencher os valores ausentes
# porque não podemos perder nenhum registro.

df.fillna({"Calories": 300}, inplace=True)

print("Valores ausentes de Calories preenchidos com 300.")


# ==========================================
# ETAPA 5 — VERIFICAR O RESULTADO
# ==========================================

print("\n===== VERIFICAÇÃO FINAL =====")

print("Valores ausentes após a limpeza:")
print(df.isna().sum())


# ==========================================
# ETAPA 6 — EXIBIR OS DADOS
# ==========================================

print("\n===== DATAFRAME FINAL =====")

print(df.to_string())