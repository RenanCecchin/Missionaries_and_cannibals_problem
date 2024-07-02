from collections import deque
from tree import Tree
from margin import Margin 
from boat import Boat
from copy import deepcopy

class Search:
    def __init__(self, start_l_margin, start_r_margin, boat_capacity):
        self.start_l_margin = start_l_margin
        self.start_r_margin = start_r_margin
        #Inicializa a margem objetivo
        self.goal_l_margin = Margin(self.start_r_margin.getMissionaries(), self.start_r_margin.getCannibals(), self.start_r_margin.getMaxMissionaries(), self.start_r_margin.getMaxCannibals(), "MargemEsquerda")
        
        self.start_boat = Boat(0, 0, boat_capacity, 1, self.start_l_margin, self.start_r_margin)

        self.tree = Tree(self.start_boat)
        self.queue = deque()
        self.queue.append(self.tree)    #Inicializa a fila e adiciona o primeiro nó

    #Realiza a busca ate encontrar o nó objetivo
    def search(self):
        while self.queue.__sizeof__() > 0:
            current_node = self.queue.popleft()             #Retorna o primeiro nó da fila
            current_boat = current_node.data                #Retorna o conteudo da arvore
            print("Estado atual: ", current_boat)
            current_margin = current_boat.margins[current_boat.margin_id]

            #Testa se o nó atual não gera falha
            if current_margin.failure() or current_boat.failure():
                continue

            #Testa se o nó atual é objetivo
            if current_boat.margins[0].getMissionaries() == self.goal_l_margin.getMissionaries() and current_boat.margins[0].getCannibals() == self.goal_l_margin.getCannibals():
                print("Caminho:")
                stack = []
                while current_node.parent is not None:      #Percorre a arvore até o nó inicial e coloca em uma pilha
                    stack.append(current_node)
                    current_node = current_node.parent
                for movement in stack:                      #Desempilha para mostrar a sequencia certa de movimentos
                    print(movement.data)
                return True

            #Gera novos estados
            self.generateNewStates(current_node)


    #Funcao que gera todas as combinacoes não-nulas de movimentos possíveis
    #levando em conta a capacidade do barco
    # @param current_node: nó atual da arvore que será expandido
    def generateNewStates(self, current_node):
        current_boat = current_node.data
        for missionaries in range(0, current_boat.capacity + 1):
            for cannibals in range(0, current_boat.capacity + 1):
                if missionaries + cannibals <= current_boat.capacity and missionaries + cannibals > 0:
                    #Faz uma copia do no atual
                    n_boat = deepcopy(current_node.data)
                    #Move o barco e aloca ele na arvore como filho do nó atual
                    n_node = Tree(n_boat.moveBoat(missionaries, cannibals), current_node)
                    #Adiciona ao final da fila
                    self.queue.append(n_node)
            