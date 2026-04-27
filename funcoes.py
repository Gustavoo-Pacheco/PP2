import random


def rolar_dados(quantidade):
    dados = []
    for i in range(quantidade):
        dado = random.randint(1, 6)
        dados.append(dado)
    return dados
