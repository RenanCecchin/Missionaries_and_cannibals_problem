from enviroment import Enviroment

class Margin(Enviroment):
    def __init__(self, missionaries, cannibals, max_missionaries, max_cannibals, name):
        super().__init__(missionaries, cannibals, max_missionaries, max_cannibals)
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.name = name

    #Metodo que move os individuos da margem atual para o barco
    # @param missionaries: numero de missionarios que serao movidos
    # @param cannibals: numero de cannibais que serao movidos
    def moveToBoat(self, missionaries, cannibals):
        self.missionaries -= missionaries
        self.cannibals -= cannibals

    #Metodo que move os inviduos do barco para a margem atual
    # @param missionaries: numero de missionarios que serao movidos
    # @param cannibals: numero de cannibais que serao movidos
    def moveFromBoat(self, missionaries, cannibals):
        self.missionaries += missionaries
        self.cannibals += cannibals

    #Metodo que mostra o estado atual da margem
    def showState(self):
        print("<{}, {}, {}>".format(self.missionaries, self.cannibals, self.name))

    def getCannibals(self):
        return self.cannibals

    def getMissionaries(self):
        return self.missionaries

    def getMaxMissionaries(self):
        return self.max_missionaries

    def getMaxCannibals(self):
        return self.max_cannibals

    def __str__(self):
        return "<{}, {}, {}>".format(self.missionaries, self.cannibals, self.name)