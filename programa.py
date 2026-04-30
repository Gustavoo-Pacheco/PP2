from funcoes import rolar_dados, guardar_dado, remover_dado, faz_jogada

cartela = {
    'regra_simples': {},
    'regra_avancada': {}
}

combinacoes_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

print("Cartela de Pontos:")
print("-" * 25)
for i in range(1, 7):
    espacos = " " * (15 - len(str(i)))
    if i in cartela['regra_simples']:
        print(f"| {i}: {espacos}| {cartela['regra_simples'][i]:02} |")
    else:
        print(f"| {i}: {espacos}|    |")
for combinacao in combinacoes_avancadas:
    espacos = " " * (15 - len(combinacao))
    if combinacao in cartela['regra_avancada']:
        print(f"| {combinacao}: {espacos}| {cartela['regra_avancada'][combinacao]:02} |")
    else:
        print(f"| {combinacao}: {espacos}|    |")
print("-" * 25)

for rodada in range(12):

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens_usadas = 0

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    jogada_feita = False
    while not jogada_feita:
        opcao = input(">")

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '3':
            if rerrolagens_usadas >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                quantidade_para_rolar = len(dados_rolados)
                dados_rolados = rolar_dados(quantidade_para_rolar)
                rerrolagens_usadas = rerrolagens_usadas + 1
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '4':
            print("Cartela de Pontos:")
            print("-" * 25)
            for i in range(1, 7):
                espacos = " " * (15 - len(str(i)))
                if i in cartela['regra_simples']:
                    print(f"| {i}: {espacos}| {cartela['regra_simples'][i]:02} |")
                else:
                    print(f"| {i}: {espacos}|    |")
            for combinacao in combinacoes_avancadas:
                espacos = " " * (15 - len(combinacao))
                if combinacao in cartela['regra_avancada']:
                    print(f"| {combinacao}: {espacos}| {cartela['regra_avancada'][combinacao]:02} |")
                else:
                    print(f"| {combinacao}: {espacos}|    |")
            print("-" * 25)
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '0':
            print("Digite a combinação desejada:")
            while True:
                combinacao = input(">")

                if combinacao in ['1', '2', '3', '4', '5', '6']:
                    chave = int(combinacao)
                    if chave in cartela['regra_simples']:
                        print("Essa combinação já foi utilizada.")
                    else:
                        todos_os_dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(todos_os_dados, combinacao, cartela)
                        jogada_feita = True
                        break

                elif combinacao in combinacoes_avancadas:
                    if combinacao in cartela['regra_avancada']:
                        print("Essa combinação já foi utilizada.")
                    else:
                        todos_os_dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(todos_os_dados, combinacao, cartela)
                        jogada_feita = True
                        break

                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

pontos_simples = 0
for valor in cartela['regra_simples'].values():
    pontos_simples = pontos_simples + valor

bonus = 0
if pontos_simples >= 63:
    bonus = 35

pontos_avancados = 0
for valor in cartela['regra_avancada'].values():
    pontos_avancados = pontos_avancados + valor

pontuacao = pontos_simples + pontos_avancados + bonus

print("Cartela de Pontos:")
print("-" * 25)
for i in range(1, 7):
    espacos = " " * (15 - len(str(i)))
    if i in cartela['regra_simples']:
        print(f"| {i}: {espacos}| {cartela['regra_simples'][i]:02} |")
    else:
        print(f"| {i}: {espacos}|    |")
for combinacao in combinacoes_avancadas:
    espacos = " " * (15 - len(combinacao))
    if combinacao in cartela['regra_avancada']:
        print(f"| {combinacao}: {espacos}| {cartela['regra_avancada'][combinacao]:02} |")
    else:
        print(f"| {combinacao}: {espacos}|    |")
print("-" * 25)
print(f"Pontuação total: {pontuacao}")