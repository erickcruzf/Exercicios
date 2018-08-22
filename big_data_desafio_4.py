#declarar classe e #minhaprimeiraárvorebinária
class Node:

    def __init__(self, data):

        self.right = None
        self.left = None
        self.data = data
    #Adiciona nós
    def add(self, data):
        #Se arvore.add(data) > arvore.data .
        if data >= self.data:
            #Se estiver sem aresta recebe uma aresta pra um novo nó.
            if self.right == None:
                self.right = Node(data)
            #Se não, avança pro próximo nó da direita e repede o método.
            else:
                self.right.add(data)
        #Se a data for menor ela vai pra esquerda.
        else:

            if self.left == None:
                self.left = Node(data)
            else:
                self.left.add(data)
    #Retorna se encontrado a váriavel search.
    def find(self, search):
        #{search} maior, lado direito.
        if search > self.data:
            #Se acabou os nós, acabou a busca.
            if self.right == None:
                return "O {} não foi encontrado.".format(search)
            else:
                self.right.find(search)
        #{earch} menor, lado esquerdo.
        if search < self.data:

            if self.left == None:
                return "O {} não foi encontrado.".format(search)
            else:
                self.left.find(search)
        #search == self.data .
        return "O {} foi encontrado.".format(search)
    #Imprimir os valores de todos os nós enquando houver informação em {data}.
    def Print(self):
        #Condição para imprimir.
        if self.left != None:
            self.left.Print()
        print(str(self.data))
        if self.right != None:
            self.right.Print()

#Árvore.
arvore = Node(3)
arvore.add(8)
arvore.add(10)
arvore.add(0)
arvore.add(15)
arvore.add(6)
arvore.add(7)
arvore.add(2)
arvore.add(3)
arvore.add(1)
arvore.add(-5)
arvore.add(-12)
arvore.add(-3)
arvore.add(2)
arvore.add(14)
print(arvore.find(7))
print(arvore.find(14))
print(arvore.find(3))
arvore.Print()

#Erick 18.08.2018
