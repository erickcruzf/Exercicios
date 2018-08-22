#Criando função:
def maquina_de_cafe(A1,A2,A3):
    #Somente entre 0 e 1000, e que seja um número inteiro.
    if (0 > (A1 or A2 or A3) > 1000) or (type(A1) or type(A2) or type(A3)) != int:
        return "Apenas números inteiros entre 0 e 1000."
    #Incluindo o térreo do prédio na lista dos andares.
    andares = ["Terreo"]
    #Recebendo a informação dos trabalhadores por andar.#Incluindo o térreo do prédio na lista dos andares.
    andares.append(A1), andares.append(A2), andares.append(A3)
    #lista de tempo por andar, None para não coincidir com algum valor na contagem.
    tempo_x_andar = [None]
    #String vazia para caso de opções de colocação.
    outro= ""
    #Número máximo de minutos para comparação. 
    menor = 6001
    #Tempo perdido para usar a máquina no primeiro andar, segundo andar e terceiro andar.
    tempo_x_andar.append(andares[2]*2 + andares[3]*4), tempo_x_andar.append(andares[1]*2 + andares[3]*2), tempo_x_andar.append(andares[1]*4 + andares[2]*2)
    #Loop passando por todos andares e registrando na string {outro} os empates, e no {menor} o andar com menos desperdício de tempo.
    for andar in range(1,len(tempo_x_andar)):
        if menor == tempo_x_andar[andar]:
            outro += " ou {andar}º andar".format(andar = andar)
            
        if menor > tempo_x_andar[andar]:
            menor = tempo_x_andar[andar]
            
    return "Seria melhor se colocado no {andar}º andar{empate}, com tempo gasto diário de {tempo} minutos.".format(andar = tempo_x_andar.index(menor),empate = outro, tempo = menor)

#ReadyToWork
#Recebe o valor de A1, A2 e A3
A1 = int(input("Digite quantas pessoas trabalham em A1: "))
A2 = int(input("Digite quantas pessoas trabalham em A2: "))
A3 = int(input("Digite quantas pessoas trabalham em A3: "))
print(maquina_de_cafe(A1, A2, A3))

#Erick 18.08.2018
