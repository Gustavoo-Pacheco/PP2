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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    nova_lista_r = []
    nova_lista_e = []
    for dado in dados_rolados:
        nova_lista_r.append(dado)
    for i in range(len(dados_no_estoque)):
        atual = dados_no_estoque[i]
        if dado_para_remover != i:
            nova_lista_e.append(atual)
        else:
            nova_lista_r.append(atual)
    return([nova_lista_r, nova_lista_e])

def calcula_pontos_regra_simples(lista_inteiros):
    resultado = {1:0,2:0,3:0,4:0,5:0,6:0}
    for face in lista_inteiros:
        if face in resultado:
            resultado[face] += (1 * face)
    return resultado

def calcula_pontos_soma(dados):
    soma = 0
    for n in dados:
        soma += n
    return soma
