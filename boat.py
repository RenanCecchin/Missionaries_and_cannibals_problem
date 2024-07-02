from enviroment import Enviroment
#Classe do barco deriva da classe ambiente
class Boat(Enviroment):
    #__init__: Construtor da classe
    # @param capacity: capacidade do barco
    # @param margin_id: id da margem que o barco esta
    # @param l_margin: referencia para a margem esquerda
    # @param r_margin: referencia para a margem esquerda
    def __init__(self, missionaries, cannibals, capacity, margin_id, l_margin, r_margin):
        self.margins = [l_margin, r_margin]
        
        #Chama a classe o construtor da classe pai
        super().__init__(missionaries, cannibals, self.margins[0].max_missionaries, self.margins[0].max_cannibals)
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.capacity = capacity
        self.margin_id = margin_id                #0: left, 1: right

    #Metodo que move os individuos da margem atual para o barco, e em seguida do barco para a outra margem
    # @param missionaries: numero de missionarios que serao movidos
    # @param cannibals: numero de cannibais que serao movidos
    def moveBoat(self, missionaries, cannibals):
        #Retira os missionarios e canibais da margem atual
        self.margins[self.margin_id].moveToBoat(missionaries, cannibals)
        self.missionaries = missionaries
        self.cannibals = cannibals
        #Muda de margem
        self.sail()

        #Adiciona os missionarios e canibais na margem atual
        self.margins[self.margin_id].moveFromBoat(missionaries, cannibals)
        return self

    #Define a falha pro programa chamando o metodo da classe pai junto com uma restricao exclusiva do barco (capacidade)
    def failure(self):
        return self.missionaries + self.cannibals > self.capacity or super().failure()

    #Metodo que muda de margem
    def sail(self):
        self.margin_id = 1 - self.margin_id

    #Metodo que mostra o estado atual do problema
    # <missionaries, cannibals, boat>
    #Os missionarios e canibais sao os que estão na margem esquerda
    def __str__(self):
        return "<{}, {}, {}>".format(self.margins[0].getMissionaries(), self.margins[0].getCannibals(), self.margins[self.margin_id].name)
