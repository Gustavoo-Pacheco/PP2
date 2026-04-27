import random


def rolar_dados(quantidade):
    dados = []
    for i in range(quantidade):
        dado = random.randint(1, 6)
        dados.append(dado)
    return dados

def guardar_dado(dados_rolados, dados_guardados, indice_dado):
    dado = dados_rolados[indice_dado]
    listanova = []
    for i in range(len(dados_rolados)):
        if i != indice_dado:
            listanova.append(dados_rolados[i])
    dados_rolados = listanova
    dados_guardados.append(dado)
    return [dados_rolados, dados_guardados]

