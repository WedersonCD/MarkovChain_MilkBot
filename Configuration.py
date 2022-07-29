import math

class Configuration:
    def __init__(self):
        self.herdTurnover= 35#média ano
        self.milkProductionLevel=10000 #kilos por ano
        self.dryPeriod= 60 #Dias de seca por ano
        self.lastDayToBreedACow= 294 #?em dias
        self.milkThreshold= 23# kilos por vaca por dia
        self.pregnancyLoss= 0.082 #?
        self.pregnancyRate= 0.146
        self.mortalityRate= 0.2 #indice de mortalidade anual
        self.voluntaryWaitingPeriod=42#in days
        self.calvingPeriodLen=180

        #economic variables
        self.replacementCost= 1300# #per call
        self.carcassBalue= 0.35
        self.calfBalue=100
        self.milkPrice=0.43
        self.feedPriceForLactatingCow=0.22
        self.feedPriceForDryCow=0.18

        #simulation variables
        self.cowInitialNumber=200
        self.days=1000
        self.stateLen= 21
        self.stateQtd=math.ceil(self.days/self.stateLen)

        #Chances de uma vaca morrer de uma troca de stado pra outro; 365=Quantidade de dias no ano
        self.mortalityRateByState=(self.mortalityRate * self.stateLen)/365

