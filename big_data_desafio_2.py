#O código diferencia acentos: a != á . O código desconsidera qualquer coisa que não seja letra, porém ele imprime a!m!a se assim for escrito, pois a "!" não interrompe o palindromo.
#O código só imprime um maior palindromo, ou seja, em caso de empate no tamanho, apenas o primeiro será impresso.

def maior_palindromo(string):
    #declarando a lista com as letras, incluindo acentos.
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "á", "é", "í", "ó", "ú", "ã", "õ", "â", "ê", "î", "ô", "û"]
    #maior palindromo
    maior = ""
    #string pra comparação
    string_teste = ""
    #marcador pra indice impar
    odd = 0
    #indices do maior palindromo na {string}
    index_inicio = 0
    index_fim = 0
    #string pra formação de palindromos sem espaços
    string2 = string.replace(" ","")
    #Condição pra strings muito pequenas
    if len(string) <= 2:
        if len(string) > 1 and string[0] == string[1]:
            return string
        return "Erro. Nenhum palindromo encontrado."

    #Primeiro loop pra pegar as letras indo de dois em dois.
    for letra in range(0,len(string),2):
        if string[letra] not in letras:
                if string[letra-1] in letras:
                    #marcador de indice
                    odd = 1
        #recebe letra percebendo se o indice é negativo.
        string_teste = string[letra - odd]
        #Segundo loop pra pegar as letras em diante.
        for i in range(letra+1,len(string)):
            #Filtro para pegar somente letras.
            if string[i] not in letras:
                continue
            #Acrescenta uma letra pela esquerda.
            string_teste = string[i] + string_teste
            
            if string_teste in string2:
                #maior é usado para identificar de forma rápida o tamanho da string.
                if len(string_teste) > len(maior) and len(string_teste) >= 3:
                    maior = string_teste
                    #indices que são usados para impressão do palindromo.
                    index_inicio = letra - odd
                    index_fim = i + 1
            #Não encontrado
            else:
                #Retorna o resultado e otimiza o número de passos para terminar o código.
                if (len(maior) + letra) > (len(string) - len(maior) or i == len(string)-1):
                    if maior + string[index_inicio-1] in string2 and index_inicio != 0:
                    #retorna o palindromo utilizando os indices.
                        return string[index_inicio-1:index_fim]
                    return string[index_inicio:index_fim]
                #Reseta e volta pro primeiro loop pra pegar a próxima letra.
                string_teste = ""
                odd = 0
                break
        #Outra saída para caso a ultima letra ser parte do palindromo, economiza 1 loop.
        else:
            if maior + string[index_inicio-1] in string2 and index_inicio != 0:
                return string[index_inicio-1:index_fim]
            return string[index_inicio:index_fim]
#Recebe uma string.
string = input("Digite uma string: ")
print(maior_palindromo(string))

#Erick 19.08.2018
