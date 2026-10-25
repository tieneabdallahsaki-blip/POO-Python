class Vehicule:
    def __init__(self, nom, vitesse_max, kilometrage):
        self.nom = nom
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

class Bus(Vehicule):
    pass

v = Bus("Ferrari", 280, 1820)
print(v.nom)
print(v.vitesse_max)
print(v.kilometrage)
