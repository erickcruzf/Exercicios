#Criação da função

def soma_dois_array(array, soma):
    #Primeiro Passo: declarei uma string vazia dentro da função pra imprimir as somas do array.
    lista_soma = ""
    #Segundo Passo: pra cada número no argumento array compara com cada outro elemento no mesmo array.
    for indice in range(0,len(array)):
        for indice2 in range(indice + 1, len(array)):
            #Terceiro Passo: adiciona números para uma lista quando a soma de 2 elementos for igual ao argumento soma.
            if array[indice] + array[indice2] == soma:
                lista_soma += " {indice} + {indice2},".format(indice = array[indice], indice2 = array[indice2])
    #Quarto Passo: condição em booleano para retornar o resultado.
    if lista_soma == "":
        return "Falso: não existe nenhuma combinação de dois elementos que some {soma}.".format(soma = soma)
    return "True:{casos}".format(casos = lista_soma[:-1])
#Recebe o array.
str_array = input("Entre com array entre parenteses: ")[1:-1].split(',')
array = [int(num) for num in str_array]
#Recebe a soma.
valor_da_soma = int(input("Digite a soma: "))
print(soma_dois_array(array, valor_da_soma))

#Complexidade do Código da Função: NLOC: 9, Complexity: 5

#Erick 18.08.2018
