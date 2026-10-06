import pandas as pd

# Carregar os dados
df = pd.read_csv("data.csv")


# ==========================================
# ATIVIDADE 1 — CONHECENDO OS DADOS
# ==========================================

print("\n===== ATIVIDADE 1 =====")

print("Todos os dados:")
print(df.to_string())

print("\nQuantidade de linhas:", len(df))
print("Quantidade de colunas:", len(df.columns))
print("Nomes das colunas:", list(df.columns))

print("\nQuantidade de registros:", len(df))


# ==========================================
# ATIVIDADE 2 — IDENTIFICANDO VALORES AUSENTES
# ==========================================

print("\n===== ATIVIDADE 2 =====")

print("Valores ausentes:")
print(df.isna())

print("\nQuantidade de valores ausentes por coluna:")
print(df.isna().sum())


# ==========================================
# ATIVIDADE 3 — UTILIZANDO dropna()
# ==========================================

print("\n===== ATIVIDADE 3 =====")

new_df = df.dropna()

print("Novo DataFrame sem valores ausentes:")
print(new_df.to_string())

print("\nDataFrame original continua com:")
print(len(df), "linhas")

print("Novo DataFrame possui:")
print(len(new_df), "linhas")

print("Linhas removidas:", len(df) - len(new_df))


# ==========================================
# ATIVIDADE 4 — dropna() COM inplace
# ==========================================

print("\n===== ATIVIDADE 4 =====")

# Criamos uma cópia para não destruir o DataFrame
df_dropna = df.copy()

df_dropna.dropna(inplace=True)

print("DataFrame após dropna(inplace=True):")
print(df_dropna.to_string())

print("\nValores ausentes após a limpeza:")
print(df_dropna.isna().sum())


# ==========================================
# ATIVIDADE 5 — UTILIZANDO fillna()
# ==========================================

print("\n===== ATIVIDADE 5 =====")

df_fill = df.copy()

df_fill.fillna(300, inplace=True)

print("DataFrame após preencher os valores ausentes com 300:")
print(df_fill.to_string())

print("\nValores ausentes após fillna():")
print(df_fill.isna().sum())


# ==========================================
# ATIVIDADE 6 — PREENCHENDO UMA COLUNA ESPECÍFICA
# ==========================================

print("\n===== ATIVIDADE 6 =====")

df_calories = df.copy()

print("Preenchendo Calories com 300:")

df_calories.fillna({"Calories": 300}, inplace=True)

print(df_calories.to_string())

print("\nValores ausentes:")
print(df_calories.isna().sum())


print("\nAgora preenchendo Calories com 350:")

df_calories_350 = df.copy()

df_calories_350.fillna({"Calories": 350}, inplace=True)

print(df_calories_350.to_string())

print("\nValores ausentes:")
print(df_calories_350.isna().sum())


# ==========================================
# ATIVIDADE 7 — COMPARANDO dropna() E fillna()
# ==========================================

print("\n===== ATIVIDADE 7 =====")

# Versão usando dropna()
df_drop = df.dropna()

print("Com dropna():")
print("Quantidade de registros:", len(df_drop))

# Versão usando fillna()
df_fillna = df.copy()

df_fillna.fillna({"Calories": 300}, inplace=True)

print("\nCom fillna():")
print("Quantidade de registros:", len(df_fillna))


# ==========================================
# ATIVIDADE 8 — ANTES E DEPOIS DA LIMPEZA
# ==========================================

print("\n===== ATIVIDADE 8 =====")

print("Valores ausentes ANTES da limpeza:")
print(df.isna().sum())

df_limpo = df.copy()

df_limpo.fillna({"Calories": 300}, inplace=True)

print("\nValores ausentes DEPOIS da limpeza:")
print(df_limpo.isna().sum())


# ==========================================
# ATIVIDADE 9 — SITUAÇÃO-PROBLEMA
# ==========================================

print("\n===== ATIVIDADE 9 =====")

df_problema = pd.read_csv("data.csv")

print("Valores ausentes antes do tratamento:")
print(df_problema.isna().sum())

# Preencher Calories com 300
df_problema.fillna({"Calories": 300}, inplace=True)

print("\nDados depois da alteração:")
print(df_problema.to_string())

print("\nValores ausentes depois do tratamento:")
print(df_problema.isna().sum())