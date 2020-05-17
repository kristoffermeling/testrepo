import datetime

class Sensor():
    #a class collecting sensor values
    def __init__(self, posval, sensorheight ):

        self.pos = posval
        self.sensorheight = sensorheight



def les_positivt_flyttall():
    tallet = -1.0
    while tallet < 0.0:
        try:
            tallet = float(input("Skriv inn et positivt flyttall: "))
            if tallet < 0.0:
                print("Tallet kan ikke være negativ. Prøv på nytt!")
        except ValueError:
            print("Du må skrive inn et tall!")
            tallet = -1.0
    return tallet

atring = "testavstrengslice"

test = atring[1:10:3]
print(test)