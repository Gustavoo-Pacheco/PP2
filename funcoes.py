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

def calcula_pontos_sequencia_alta(dados):
    faces_unicas = []
    for d in dados:
        if d not in faces_unicas:
            faces_unicas.append(d)
    sequencias = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
    for seq in sequencias:
        encontrou = True
        for n in seq:
            if n not in faces_unicas:
                encontrou = False
        if encontrou:
            return 30
    return 0

def calcula_pontos_sequencia_baixa(dados):
    faces_unicas = []
    for d in dados:
        if d not in faces_unicas:
            faces_unicas.append(d)
    sequencias = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    for seq in sequencias:
        encontrou = True
        for n in seq:
            if n not in faces_unicas:
                encontrou = False
        if encontrou:
            return 15
    return 0

def calcula_pontos_full_house(dados):
    contagens = {}
    for d in dados:
        if d in contagens:
            contagens[d] +=1
        else:
            contagens[d] = 1
    
    valores = contagens.values()

    if 3 in valores and 2 in valores:
        total = 0
        for d in dados:
            total += d
        return total
    else:
        return 0
    
def calcula_pontos_quadra(dados):
    contagens = {}
    for d in dados:
        if d in contagens:
            contagens[d] += 1
        else:
            contagens[d] = 1
    
    quadra = False
    for qtd in contagens.values():
        if qtd >= 4:
            quadra = True
    
    if quadra:
        total = 0
        for d in dados:
            total += d
        return total

    return 0

def calcula_pontos_quina(dados):
    contagens = {}
    for d in dados:
        if d in contagens:
            contagens[d] += 1
        else:
            contagens[d] = 1

    for qtd in contagens.values():
        if qtd >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados),
    }