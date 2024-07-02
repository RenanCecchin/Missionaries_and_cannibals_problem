#Classe pai de todos os ambientes(margem e barco)
class Enviroment:
    #__init__: Construtor da classe
    # @param missionaries: numero de missionarios na margem
    # @param cannibals: numero de cannibais na margem
    # @param max_missionaries: numero maximo de missionarios na margem
    # @param max_cannibals: numero maximo de cannibais na margem
    def __init__(self, missionaries, cannibals, max_missionaries, max_cannibals):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.max_missionaries = max_missionaries
        self.max_cannibals = max_cannibals
    
    #Metodo que checa falhas
    # @return: True se falhar, False se não falhar
    def failure(self):
        return (self.missionaries < self.cannibals and self.missionaries != 0)\
            or self.missionaries < 0\
                 or self.cannibals < 0\
                     or self.max_cannibals < self.cannibals\
                        or self.max_missionaries < self.missionaries