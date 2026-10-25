class Vehicule:
    def __init__ (self, vitesse_max, kilometrage):
        self.vitesse_max = vitesse_max
        self.kilometrage = kilometrage

v = Vehicule(250, 1900)
print(v.vitesse_max, v.kilometrage)
      
