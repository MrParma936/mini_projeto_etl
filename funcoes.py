import csv
import re
from datetime import datetime

# As funções estão ordenadas pela ordem alfabética do nome para facilitar a localização


def contar_repetidos(lista, posicao):
    contagem = {}

    for linha in lista:
        if linha[posicao] in contagem:
            contagem[linha[posicao]]  += 1
        else:
            contagem[linha[posicao]] = 1

    ordenado = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
    for chave, valor in ordenado:
        print(f"> {repr(chave)} - {valor}")


def filtrar(lista, posicao):
    
    categorias = sorted(set(linha[posicao] for linha in lista))

    print(categorias)


def filtrar_nulos(lista, posicao):
    nulos = ["", "null", "nan"]
    encontrados = {}

    for linha in lista:
        valor = linha[posicao].strip().lower()

        if valor in nulos:

            if valor in encontrados:
                encontrados[valor] += 1
            else:
                encontrados[valor] = 1

    print(f">>>>>>>> Na coluna {posicao} temos os seguintes valores nulos com seu número de ocorrências: ")

    for chave, valor in encontrados.items():
        print(f"> {repr(chave)}: {valor}")


def imprimir_pedidos(dicionario):
    for i, item in enumerate(dicionario):
        print(f"{i+1} ->")
        print(f"order_id: {item['order_id']}")
        print(f"customer_id: {item['customer_id']}")
        print(f"order_status: {item['order_status']}")
        print(f"order_purchase_timestamp: {item['order_purchase_timestamp']}")
        print(f"order_approved_at: {item['order_approved_at']}")
        print(f"order_delivered_carrier_date: {item['order_delivered_carrier_date']}")
        print(f"order_delivered_customer_date: {item['order_delivered_customer_date']}")
        print(f"order_estimated_delivery_date: {item['order_estimated_delivery_date']}\n")

        if i == 4:
            break


def imprimir_produtos(dicionario):
    for i, item in enumerate(dicionario):
        print(f"{i+1} ->")
        print(f"product_id: {item['product_id']}")
        print(f"product_category_name: {item['product_category_name']}")
        print(f"product_name_lenght: {item['product_name_lenght']}")
        print(f"product_description_lenght: {item['product_description_lenght']}")
        print(f"product_photos_qty: {item['product_photos_qty']}")
        print(f"product_weight_g: {item['product_weight_g']}")
        print(f"product_length_cm: {item['product_length_cm']}")
        print(f"product_height_cm: {item['product_height_cm']}")
        print(f"product_width_cm: {item['product_width_cm']}\n")

        if i == 4:
            break


def informar_tamanho(arquivo):
    tamanho = len(arquivo)
    print(f">>>>>>>> O arquivo possui {tamanho} registros.\n")


def normalizar_data(lista, posicao):

    for linha in lista:
        if linha[posicao] != "":
            data = str(linha[posicao]).strip()
            
            data_normalizada = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            data = data_normalizada.strftime("%d/%m/%Y")

            linha[posicao] = data

    return lista


def normalizar_nomes(lista, posicao):

    for linha in lista:
        normalizado = str(linha[posicao]).lower().strip()
        normalizado = re.sub(r"[^\w\s]", "", normalizado)
        normalizado = re.sub(r"\s+", " ", normalizado).strip()

        linha[posicao] = normalizado

    return lista


def remover_linhas_com_nulos(lista, colunas_numericas):

    lista_limpa = []

    for linha in lista:

        tem_invalido = False

        for coluna in colunas_numericas:

            valor = str(linha[coluna]).strip()

            try:
                float(valor)

            except ValueError:
                tem_invalido = True

        if not tem_invalido:
            lista_limpa.append(linha)

    return lista_limpa


def salvar_arquivo(nome_arquivo):
    dados = []

    with open(nome_arquivo, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            dados.append(linha)

    return dados


def substituir(lista, posicao):
    substituida = []

    for linha in lista:
        if linha[posicao] == "":
            linha[posicao] = "Sem Categoria"

        substituida.append(linha)
                
    return substituida


def vazios_por_status(lista, posicao1, posicao2):
    #status = []
    contagem = {}

    for linha in lista:
        data = linha[posicao1]
        status = linha[posicao2]

        if data == "":
            if status in contagem:
                contagem[status] += 1
            else:
                contagem[status] = 1

    ordenado = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    for chave, valor in ordenado:
        print(f"> {repr(chave)} - {valor}")


def verificar_formato_data(lista, posicao):
    variacoes_formato = set()

    for linha in lista:
        valor = str(linha[posicao]).strip()

        try:
            datetime.strptime(valor, "%Y-%m-%d %H:%M:%S")

        except ValueError:
            variacoes_formato.add(valor)

    if list(variacoes_formato) == [] or list(variacoes_formato) == [""]:
        print("> Nenhum formato de data diferente de %Y-%m-%d %H:%M:%S foi encontrado!\n")

    return list(variacoes_formato)


def verificar_invalidos(lista, posicao):
    encontrados = {}

    for linha in lista:

        valor = linha[posicao].strip().lower()

        try:
            float(valor)

        except ValueError:
            encontrados[valor] = encontrados.get(valor, 0) + 1

    print(f"\n>>>>>>>> Na coluna {posicao} temos os seguintes valores nulos com seu número de ocorrências: ")

    for chave, valor in encontrados.items():
        print(f"> {repr(chave)}: {valor}")


def sumario_estatistico(lista, posicao, posicao2):
    linhas_processadas = len(lista)
    registros_corrigidos = 0
    pedidos_cancelados = 0

    for linha in lista:
        if linha[posicao].lower().strip() != "":
            registros_corrigidos += 1

    for linha in lista:
        if linha[posicao2].lower().strip() == "canceled":
            pedidos_cancelados += 1
       
    print(f"> Contagem total de linhas processadas: {linhas_processadas}")
    print(f"> Total de registros de data normalizados: {registros_corrigidos}")
    print(f"> Total de pedidos cancelados identificados: {pedidos_cancelados}\n")





























    


