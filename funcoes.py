import csv
import re
from datetime import datetime

# As funções estão ordenadas pelo nome em ordem alfabética para facilitar a localização


def contar_repetidos(lista, posicao):
    """
    Conta a quantidade de ocorrências de cada valor presente em uma determinada posição das linhas de uma lista.

    Parâmetros:
        lista (list): Lista contendo os registros.
        posicao (int): Índice da coluna que será analisada.

    Saída:
        Exibe os valores encontrados e suas respectivas quantidades de ocorrência em ordem decrescente.
    """

    contagem = {} # dicionário vazio que vai receber pares de chave (cada novo valor encontrado) e valor (quantidade de ocorrências desse valor)

    for linha in lista: # percorre cada linha da lista recebida
        if linha[posicao] in contagem: # verifica se o valor da posição na linha já existe como chave no dicionário
            contagem[linha[posicao]]  += 1 # se já existir incrementa a quantidade em 1
        else:
            contagem[linha[posicao]] = 1 # se for a primeira ocorrência cria a chave com valor inicial 1

    # converte o dicionário em uma lista de tuplas e ordena pela quantidade de ocorrências do maior para o menor
    ordenado = sorted(contagem.items(), key=lambda item: item[1], reverse=True) 
    for chave, valor in ordenado: # percorre a lista ordenada 
        print(f"> {repr(chave)} - {valor}") # exibe os resultados


def filtrar_unicos(lista, posicao):
    """
    Exibe os valores únicos presentes em uma determinada posição das linhas da lista.

    Parâmetros:
        lista (list): Lista contendo os registros.
        posicao (int): Índice da coluna a ser analisada.

    Saída:
        Exibe uma lista ordenada contendo apenas os valores distintos encontrados.
    """ 
    
    # percorre todas as linhas da lista e extrai os valores da posição informada
    categorias = sorted(set(linha[posicao] for linha in lista)) # set() remove valores repetidos e sorted() ordena os resultados em ordem alfabética

    print(categorias) # exibe a lista de valores únicos encontrados


def filtrar_nulos(lista, posicao):
    """
    Identifica e contabiliza valores nulos em uma coluna específica.

    São considerados nulos:
    - string vazia ""
    - "null"
    - "nan"

    Antes da verificação, os valores são normalizados removendo espaços em branco e convertendo para minúsculas.

    Parâmetros:
        lista (list): Lista contendo os registros.
        posicao (int): Índice da coluna a ser analisada.

    Saída:
        Exibe cada tipo de valor nulo encontrado e sua quantidade de ocorrências.
    """

    nulos = ["", "null", "nan"] # lista com os valores que serão considerados nulos
    encontrados = {} # dicionário que armazenará chave (tipo de valor nulo encontrado) e valor (quantidade de ocorrências desse tipo)

    for linha in lista: # percorre todas as linhas da lista
        valor = linha[posicao].strip().lower() # remove espaços extras e converte para minúsculas para padronizar a comparação

        if valor in nulos: # verifica se o valor atual é considerado nulo

            if valor in encontrados: # verifica se o valor da posição na linha já existe como chave no dicionário
                encontrados[valor] += 1 # se já existir incrementa a quantidade em 1
            else:
                encontrados[valor] = 1 # se for a primeira ocorrência cria a chave com valor inicial 1
       
    print(f">>>>>>>> Na coluna {posicao} temos os seguintes valores nulos com seu número de ocorrências: ") # exibe o cabeçalho do relatório

    for chave, valor in encontrados.items(): # percorre o dicionário
        print(f"> {repr(chave)}: {valor}") # exibe os resultados


def imprimir_pedidos(dicionario):
    """
    Exibe os cinco primeiros registros do dataset de pedidos.

    A função percorre uma lista de dicionários contendo informações dos pedidos e imprime seus campos de forma organizada.

    Parâmetros:
        dicionario (list): Lista de dicionários representando os pedidos.

    Saída:
        Exibe na tela os cinco primeiros registros encontrados.
    """
     
    for i, item in enumerate(dicionario): # percorre a lista de dicionários utilizando enumerate() para obter simultaneamente o índice e o item
        # exibe a numeração do registro iniciando em 1
        print(f"{i+1} ->") 
        # exibe os campos do pedido
        print(f"order_id: {item['order_id']}")
        print(f"customer_id: {item['customer_id']}")
        print(f"order_status: {item['order_status']}")
        print(f"order_purchase_timestamp: {item['order_purchase_timestamp']}")
        print(f"order_approved_at: {item['order_approved_at']}")
        print(f"order_delivered_carrier_date: {item['order_delivered_carrier_date']}")
        print(f"order_delivered_customer_date: {item['order_delivered_customer_date']}")
        print(f"order_estimated_delivery_date: {item['order_estimated_delivery_date']}\n")

        if i == 4: # interrompe a repetição após exibir os 5 primeiros registros (índices de 0 a 4)
            break


def imprimir_produtos(dicionario):
    """
    Exibe os cinco primeiros registros do dataset de produtos.

    A função percorre uma lista de dicionários contendo informações dos produtos e imprime seus campos de forma organizada.

    Parâmetros:
        dicionario (list): Lista de dicionários representando os produtos.

    Saída:
        Exibe na tela os cinco primeiros registros encontrados.
    """

    for i, item in enumerate(dicionario): # percorre a lista de dicionários utilizando enumerate() para obter simultaneamente o índice e o item
        # exibe a numeração do registro iniciando em 1
        print(f"{i+1} ->")
        # exibe os campos do produto
        print(f"product_id: {item['product_id']}")
        print(f"product_category_name: {item['product_category_name']}")
        print(f"product_name_lenght: {item['product_name_lenght']}")
        print(f"product_description_lenght: {item['product_description_lenght']}")
        print(f"product_photos_qty: {item['product_photos_qty']}")
        print(f"product_weight_g: {item['product_weight_g']}")
        print(f"product_length_cm: {item['product_length_cm']}")
        print(f"product_height_cm: {item['product_height_cm']}")
        print(f"product_width_cm: {item['product_width_cm']}\n")

        if i == 4: # interrompe a repetição após exibir os 5 primeiros registros (índices de 0 a 4)
            break


def informar_tamanho(lista):
    """
    Exibe a quantidade de registros presentes no dataset.

    A função utiliza a função nativa len() para contar quantos elementos existem na estrutura de dados carregada em memória.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.

    Saída:
        Exibe na tela a quantidade total de registros.
    """

    tamanho = len(lista) # obtém a quantidade de elementos da lista
    print(f">>>>>>>> O arquivo possui {tamanho} registros.\n") # exibe o total de registros encontrados


def normalizar_data(lista, posicao):
    """
    Converte datas de uma coluna para o formato brasileiro.

    A função percorre os registros do dataset e transforma datas no formato 'AAAA-MM-DD HH:MM:SS' para o formato 'DD/MM/AAAA'.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna que contém as datas.

    Retorno:
        list: Lista com as datas normalizadas.
    """

    for linha in lista:  # percorre todas as linhas da lista
        if linha[posicao] != "": # verifica se o campo possui uma data válida para não tentar converter valores vazios
            data = str(linha[posicao]).strip() # converte o valor para string e remove espaços extras
            
            data_normalizada = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")  # converte a string para um objeto datetime no formato original do dataset
            data = data_normalizada.strftime("%d/%m/%Y") # formata a data para o padrão brasileiro

            linha[posicao] = data # atualiza o valor na própria lista

    return lista # retorna a lista com as datas já normalizadas


def normalizar_nomes(lista, posicao):
    """
    Padroniza os textos de uma coluna do dataset.

    A função realiza as seguintes transformações:
    - converte o texto para letras minúsculas;
    - remove espaços extras no início e no final;
    - remove caracteres especiais e pontuações;
    - substitui múltiplos espaços consecutivos por um único espaço.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna que será normalizada.

    Retorno:
        list: Lista com os valores textuais padronizados.
    """

    for linha in lista: # percorre todas as linhas da lista
        normalizado = str(linha[posicao]).lower().strip() # converte o texto para minúsculas e remove espaços em branco no início e no final
        normalizado = re.sub(r"[^\w\s]", "", normalizado) # remove caracteres especiais e pontuações, mantendo apenas letras, números e espaços
        normalizado = re.sub(r"\s+", " ", normalizado).strip() # substitui múltiplos espaços consecutivos por um único espaço

        linha[posicao] = normalizado # atualiza o valor na própria lista

    return lista # retorna a lista com os textos normalizados


def remover_linhas_invalidas(lista, colunas_numericas):
    """
    Remove registros que possuem valores inválidos em colunas numéricas.

    A função percorre as colunas informadas e tenta converter seus valores para o tipo float. Caso alguma conversão falhe, o registro é 
    considerado inconsistente e não é incluído na lista final.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        colunas_numericas (list): Lista com os índices das colunas que devem conter valores numéricos.

    Retorno:
        list: Nova lista contendo apenas os registros válidos.
    """

    lista_limpa = [] # lista que armazenará apenas os registros válidos

    for linha in lista: # percorre todas as linhas do dataset

        tem_invalido = False # variável de controle para indicar se foi encontrado algum valor inválido na linha atual

        for coluna in colunas_numericas:  # percorre as colunas que devem conter números

            valor = str(linha[coluna]).strip() # converte o valor para string e remove espaços extras

            try:
                float(valor) # tenta converter o valor para número decimal
            
            except ValueError: # caso a conversão falhe, o valor não é numérico
                if valor.lower() in ["", "null", "nan"]: # como a string "nan" não gera ValueError, mais uma verificação é feita
                    tem_invalido = True # a linha é marcada como inválida

        if not tem_invalido: # se nenhum valor inválido foi encontrado 
            lista_limpa.append(linha) # adiciona a linha à lista final

    return lista_limpa # retorna apenas os registros válidos


def ler_arquivo(nome_arquivo):
    """
    Lê um arquivo CSV e armazena seus registros em uma lista.

    A função utiliza csv.DictReader para converter cada linha do arquivo em um dicionário, utilizando os nomes das colunas como chaves.

    Parâmetros:
        nome_arquivo (str): Caminho ou nome do arquivo CSV.

    Retorno:
        list: Lista de dicionários contendo os registros do arquivo.
    """

    dados = [] # lista que armazenará todos os registros do arquivo

    with open(nome_arquivo, encoding="utf-8") as arquivo: # abre o arquivo em modo leitura utilizando codificação UTF-8
        leitor = csv.DictReader(arquivo) # cria um leitor que interpreta a primeira linha como cabeçalho e retorna cada registro como um dicionário

        for linha in leitor: # percorre todas as linhas do arquivo
            dados.append(linha) # adiciona cada registro à lista de dados

    return dados # retorna a lista contendo todos os registros lidos


def substituir(lista, posicao):
    """
    Substitui valores vazios de uma coluna por um valor padrão.

    A função percorre todos os registros do dataset e verifica se a coluna informada está vazia. Quando isso ocorre, o valor é substituído 
    por "Sem Categoria".

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna que será analisada.

    Retorno:
        list: Lista com os valores vazios substituídos.
    """

    substituida = [] # lista que armazenará os registros atualizados

    for linha in lista: # percorre todas as linhas do dataset
        if str(linha[posicao]).strip() == "": # checa a ocorrência de valor vazio
           linha[posicao] = "Sem Categoria" # se houver substitui o valor vazio por um texto padrão

        substituida.append(linha) # adiciona a linha (alterada ou não) à nova lista
                
    return substituida # retorna a lista com as substituições realizadas


def sumario_estatistico(lista, posicao, posicao2):
    """
    Gera um resumo estatístico das informações processadas.

    A função calcula:
    - quantidade total de registros;
    - quantidade de registros que tiveram a data normalizada;
    - quantidade de registros com status cancelado.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna de datas que foi normalizada.
        posicao2 (int): Índice da coluna de status do pedido.

    Saída:
        Exibe na tela um resumo das estatísticas calculadas.
    """

    linhas_processadas = len(lista) # conta a quantidade total de registros processados
    registros_corrigidos = 0 # inicializa o contador de datas preenchidas
    pedidos_cancelados = 0 # inicializa o contador de pedidos com status cancelado

    for linha in lista:  # percorre os registros da lista (todos os valores foram tratados anteriormente pela função normalizar_data())
        if linha[posicao].lower().strip() != "": # verifica se os registros são válidos
            registros_corrigidos += 1 # incrementa a quantidade em 1

    for linha in lista:  # percorre os registros da lista 
        if linha[posicao2].lower().strip() == "canceled": # verifica se o status atende a condição
            pedidos_cancelados += 1 # incrementa a quantidade em 1

    # exibe o resumo estatístico   
    print(f"> Contagem total de linhas processadas: {linhas_processadas}")
    print(f"> Total de registros de data normalizados: {registros_corrigidos}")
    print(f"> Total de pedidos cancelados identificados: {pedidos_cancelados}\n")


def vazios_por_status(lista, posicao1, posicao2):
    """
    Analisa a relação entre valores vazios e o status dos pedidos.

    A função identifica registros que possuem uma determinada coluna vazia e contabiliza quantas vezes cada status aparece nesses registros.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao1 (int): Índice da coluna que será verificada quanto a valores vazios.
        posicao2 (int): Índice da coluna que contém o status.

    Saída:
        Exibe os status encontrados e suas respectivas quantidades de ocorrência, em ordem decrescente.
    """
    
    contagem = {} # dicionário vazio que vai receber pares de chave (status do pedido) e valor (quantidade de registros com data vazia)

    for linha in lista: # percorre todos os registros do dataset
        data = linha[posicao1] # obtém a data da posição informada
        status = linha[posicao2] # obtém o status da posição informada

        if data == "": # verifica se a data está vazia
            if status in contagem: 
                contagem[status] += 1 # se já existir incrementa a quantidade em 1
            else:
                contagem[status] = 1 # se for a primeira ocorrência cria a chave com valor inicial 1

    # converte o dicionário em uma lista de tuplas e ordena pela quantidade de ocorrências do maior para o menor
    ordenado = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    for chave, valor in ordenado: # percorre a lista ordenada
        print(f"> {repr(chave)} - {valor}") # exibe os resultados


def verificar_formato_data(lista, posicao):
    """
    Verifica a existência de datas fora do padrão esperado.

    A função percorre uma coluna do dataset e tenta converter seus valores para o formato '%Y-%m-%d %H:%M:%S'. Valores que não puderem ser 
    convertidos são armazenados para análise.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna que contém as datas.

    Retorno:
        list: Lista contendo os valores que não seguem o formato esperado.
    """

    variacoes_formato = set() # conjunto utilizado para armazenar formatos inválidos encontrados, o uso de set() evita registros duplicados.

    for linha in lista: # percorre todos os registros da lista
        valor = str(linha[posicao]).strip() # obtém o valor da coluna informada e remove espaços extras

        try:
            datetime.strptime(valor, "%Y-%m-%d %H:%M:%S") # tenta converter a data utilizando o formato esperado

        except ValueError: # caso a conversão falhe
            variacoes_formato.add(valor) # armazena o valor encontrado para posterior análise

    if not variacoes_formato or variacoes_formato == {""}: # verifica se nenhuma variação além de vazio foi encontrada
        print("> Nenhum formato de data diferente de %Y-%m-%d %H:%M:%S foi encontrado.\n") # em caso positivo exibe uma mensagem

    return list(variacoes_formato)  # retorna a lista de formatos diferentes encontrados


def verificar_invalidos(lista, posicao):
    """
    Identifica valores não numéricos em uma coluna do dataset.

    A função percorre todos os registros da coluna informada e tenta converter seus valores para float. Valores que não puderem ser convertidos
    são considerados inválidos e têm suas ocorrências contabilizadas.

    Parâmetros:
        lista (list): Lista contendo os registros do dataset.
        posicao (int): Índice da coluna numérica a ser analisada.

    Saída:
        Exibe os valores inválidos encontrados e suas respectivas quantidades de ocorrência.
    """

    encontrados = {} # dicionário vazio que vai receber pares de chave (cada novo valor inválido) e valor (quantidade de ocorrências desse valor)

    for linha in lista: # percorre todos os registros do dataset

        valor = linha[posicao].strip().lower() # padroniza o valor removendo espaços extras e convertendo para minúsculas

        try:
            float(valor) # tenta converter o valor para número decimal

        except ValueError: 
            if valor in encontrados: # verifica se o valor da posição na linha já existe como chave no dicionário
                encontrados[valor] += 1 # se já existir incrementa a quantidade em 1
            else:
                encontrados[valor] = 1 # se for a primeira ocorrência cria a chave com valor inicial 1

    # exibe o cabeçalho do relatório
    print(f"\n>>>>>>>> Na coluna {posicao} temos os seguintes valores inválidos com seu número de ocorrências: ")

    for chave, valor in encontrados.items(): # percorre a lista
        print(f"> {repr(chave)}: {valor}") # exibe os valores encontrados e suas quantidades
