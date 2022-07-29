import csv

class Util:
    def __init__(self):
        self

    def generateCSV(self,states):
        with open('detalhado_csv.csv','w',encoding='UTF8',newline='') as f:
            writer = csv.writer(f)

            headers=['stateNumber','cowId','cowAge','isDead','isBorned','isPregnant','isElegibleForInsemination','isOnVoluntaryWaitingPeriod','isAborted','ageLastCalving','ageLastPregnancy']
            writer.writerow(headers)
            
            data=[]
            for state in states:
                for cow in state.cowArrayTotal:
                    data.append(state.stateNumber)
                    data.append(cow.id)
                    data.append(cow.age)
                    data.append(cow.isDead)
                    data.append(cow.isBorned)
                    data.append(cow.isPregnant)
                    data.append(cow.isElegibleForInsemination)
                    data.append(cow.isOnVoluntaryWaitingPeriod)
                    data.append(cow.isAborted)
                    data.append(cow.ageLastCalving)
                    data.append(cow.ageLastPregnancy)
                    writer.writerow(data)
                    data=[]

            f.close()

    def iniciarEval(self):
        evaluar=""
        while 1:
            a=input('1 add linha 2 limpar 3 evaluar 4 add linha com tab:')
            if a=='1':
                evaluar=evaluar+'\n'+input()
            if a=='2':
                evaluar=""
            if a=='3':
                eval(evaluar)
                evaluar=""
            if a=='4':
                evaluar=evaluar+'\n\t'+input()
    

