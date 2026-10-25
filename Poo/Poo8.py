class Vehicule:
    def __init__(self, nom, vitesse_max, kilometrage):
        self.nom = nom
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

    def nombre_de_places(self, capacite):
        return f"La capacité de {self.nom} est {capacite} passagers"


class Bus(Vehicule):
    def nombre_de_places(self, capacite = 50):
        return f"La capacité de {self.nom} est {capacite} passagers"

b01 = Bus("Bus Rouge", 120, 200000)
b02 = Bus("Bus Blanc", 130, 250000)
print(b01.nombre_de_places())      
print(b02.nombre_de_places(40))    