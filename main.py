import pandas as pd 

Escola = pd.Series(
    [10, 10, 9, 9, 9],
    ['Bernardo', 'Nicolas', 'Mayron', 'Maria', 'Duda']
)

print(Escola)

#--------

Consumo_agua = pd.Series(
    [ '2l Bernardo', '3l Nicolas', '6l Mayron', '1l Maria', '2l Duda'], 
    index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
)

print(Consumo_agua)

#---------

# DataFrame - A tabela completa, com linhas e colunas, o formato que alimenta praticamente todo o gráfico e painel q vcs vão construir.
dado_loja = pd.DataFrame({ 
    'Produto': [ 'Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Preço': [ 4500, 300, 1500, 800],
    'Estoque': [ 15, 120, 3000, 20]
})

df_loja = dado_loja

df_loja['Valor_Total'] = df_loja['Preço'] * df_loja['Estoque']

print(df_loja)
# -----
df_pessoas = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego'],
    'Idade': [25, 32, 19, 41]
})

print(df_pessoas)

#-----------

df_pessoas = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego'],
    'Idade': [25, 32, 19, 41]
})

print(df_pessoas)
#---------

df_funcionarios = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elena', 'Fábio'],
    'Cargo': ['Analista', 'Gerente', 'Desenvolvedor', 'Analista', 'Diretora', 'Estagiário'],
    'Salario': [4500, 8500, 6200, 4300, 12000, 1800]
})

print(df_funcionarios.head(3))

print(df_funcionarios.tail(2))
#---------

df_funcionarios.info()

df_funcionarios['Idade'] = [25, 40, 30, 22, 45, 19]

print(df_funcionarios.describe())
#----------

df_vendas = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
    'Quantidade': [3, 10, 5, 2],
    'Valor': [4500, 150, 300, 900]
})

produtos = df_vendas['Produto']
print(produtos)

sub_df = df_vendas[['Produto', 'Valor']]
print(sub_df)
#---------

df_produtos = pd.DataFrame({
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Cabo HDMI'],
    'Estoque': [15, 120, 3000, 8, 5]
})

produtos_baixo_estoque = df_produtos[df_produtos['Estoque'] < 10]
print(produtos_baixo_estoque)

df_vendas2 = pd.DataFrame({
    'Preco': [4500, 150, 300, 900],
    'Quantidade': [3, 10, 5, 2]
})

df_vendas2['Valor_Total'] = df_vendas2['Preco'] * df_vendas2['Quantidade']
print(df_vendas2)
#---------

df_filiais = pd.DataFrame({
    'Filial': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador'],
    'Cidade': ['SP', 'RJ', 'MG', 'PR', 'BA'],
    'Faturamento_Milhares': [250, 180, 90, 60, 130]
})

# Resumo estatístico
print(df_filiais.describe())

# Filiais com faturamento acima de 100 mil
filiais_alto_faturamento = df_filiais[df_filiais['Faturamento_Milhares'] > 100]
print(filiais_alto_faturamento)