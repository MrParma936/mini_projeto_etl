import funcoes

# Criando uma lista de dicionários para armazenar o dataset de produtos
df_products = funcoes.salvar_arquivo("olist_products_dataset.csv")

# Criando uma lista de dicionários para armazenar o dataset de pedidos
df_orders = funcoes.salvar_arquivo("olist_orders_dataset.csv")

# Visualização em tela dos 5 primeiros registros do dataset de produtos
print("\n>>>>>>>> Visualização dos primeiros registros do dataset de produtos:\n")
funcoes.imprimir_produtos(df_products)

# Demonstração em tela da quantidade de registros do dataset de produtos
funcoes.informar_tamanho(df_products)

# Visualização das categorias e número de ocorrências. Strings nulas não foram identificadas, apenas valores vazios
print(">>>>>>>> A coluna product_category_name está distribuída entre os seguintes valores, ordenados pelo número de ocorrências:\n")
funcoes.contar_repetidos(df_products, "product_category_name")

# Chamada de função para substituir os valores vazios pela string 'Sem Categoria'
df_products_subst = funcoes.substituir(df_products, "product_category_name")

# Nova visualização das categorias e número de ocorrências, agora sem valores vazios
print("\n>>>>>>>> Campos nulos não foram encontrados, e os vazios foram preenchidos com a string 'Sem Categoria'\n")
funcoes.contar_repetidos(df_products_subst, "product_category_name")

# O grande número de ocorrência de valores únicos nas colunas de dimensões físicas, torna inviável a exibição como feita na coluna de categorias
# Dessa forma será aplicada função para verificar a ocorrência de valores vazios ou nulos
# Chamando função para verificar ocorrências de valores nulos na coluna 'product_weight_g'
funcoes.verificar_invalidos(df_products_subst, "product_weight_g")

# Chamando função para verificar ocorrências de valores nulos na coluna 'product_length_cm'
funcoes.verificar_invalidos(df_products_subst, "product_length_cm")

# Chamando função para verificar ocorrências de valores nulos na coluna 'product_height_cm'
funcoes.verificar_invalidos(df_products_subst, "product_height_cm")

# Chamando função para verificar ocorrências de valores nulos na coluna 'product_width_cm'
funcoes.verificar_invalidos(df_products_subst, "product_width_cm")

# Valores nulos não foram encontrados, apenas vazios, e devido a baixa incidência será feito o descarte desses registros
# Tendo em vista que o preenchimento com média ou mediana pode trazer enviesamento, diante da baixa perda de registros o descarte se mostra a melhor opção
df_products_sem_nulos = funcoes.remover_linhas_com_nulos(df_products_subst, ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"])

# Comparando o tamanho dos datasets antes e depois de remoção dos registros com valores nulos
print("\n>>>>>>>> Comparação após opção pelo descarte dos registros com nulos: ")
len_antes = (len(df_products_subst))
len_atual = (len(df_products_sem_nulos))
print(f"\n> Antes da remoção dos nulos o dataset tinha {len_antes} registros.")
print(f"> Após a remoção dos nulos o dataset tem {len_atual} registros.\n")

# Aplicando normalização nos nomes das categorias: 
# Eliminando qualquer incidência de letra maiúscula
# Removendo espaços em branco excedentes no início e no fim das strings
# Limpando eventuais caracteres especiais ou pontuações indevidas
df_products_sem_nulos = funcoes.normalizar_nomes(df_products_sem_nulos, "product_category_name")
# Visualizando resultado após a normalização 
print(">>>>>>>> Visualização dos valores na coluna product_category_name após aplicação de normalização nos nomes:\n")
funcoes.filtrar(df_products_sem_nulos, "product_category_name")

# Visualização em tela dos 5 primeiros registros do dataset de pedidos
print("\n>>>>>>>> Visualização dos primeiros registros do dataset de pedidos:\n")
funcoes.imprimir_pedidos(df_orders)

# Demonstração em tela da quantidade de registros do dataset de produtos
funcoes.informar_tamanho(df_orders)

# Verificando a ocorrência de datas de entrega vazias, conforme identificado pela diretoria
# Chamando função para verificar ocorrências de valores nulos na coluna 'order_delivered_customer_date'
funcoes.filtrar_nulos(df_orders, "order_delivered_customer_date")

# Verificando a ocorrência de status de pedido cancelado 
# Visualização dos status de pedido e número de ocorrências. Strings nulas não foram identificadas, apenas valores vazios
print("\n>>>>>>>> A coluna order_status está distribuída entre os seguintes valores, ordenados pelo número de ocorrências:\n")
funcoes.contar_repetidos(df_orders, "order_status")

# Refutada a hipótese levantada de que as datas estariam nulas devido ao status do pedido (order_status) constar como cancelado (canceled)
# Dos 2.965 registros com datas vazias, apenas 619 estão associados ao status canceled
print("\n>>>>>>>> Por esses números já fica claro que as datas de entrega vazias não tem relação com o status de pedido cancelado conforme a hipótese levantada")
# Chamando função para exibir status e número de ocorrências nos registros sem data de entrega 
print(">>>>>>>> O que fica evidenciado pela demonstração da relação dos 2.965 registros com os status, ordenados pelo número de ocorrências:\n")
funcoes.vazios_por_status(df_orders, "order_delivered_customer_date", "order_status")

# Os primeiros registros exibidos do dataset apresentam a coluna order_approved_at com o formato de data no padrão "%Y-%m-%d %H:%M:%S"
# Chamando função para verificar se esse padrão se repete em todos os registros
print("\n>>>>>>>> Verificação de formatos de data na coluna order_approved_at:")
funcoes.verificar_formato_data(df_orders, "order_approved_at")

# Chamando função para converter o formato de data
df_orders_data_norm = funcoes.normalizar_data(df_orders, "order_approved_at")
# Exibindo o novo formato de data nos primeiros 5 registros do dataset
print("Exibindo os primeiros registros do dataset com a data normalizada na coluna order_approved_at:\n")
funcoes.imprimir_pedidos(df_orders_data_norm)

print(">>>>>>>> Sumário estatístico:\n")
# Chamando função para verificar a sanitização, exibindo a contagem de linhas processadas, registros corrigidos e pedidos com status cancelado
funcoes.sumario_estatistico(df_orders, "order_approved_at", "order_status")






