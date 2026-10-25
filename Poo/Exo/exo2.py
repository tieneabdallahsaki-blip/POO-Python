class Voitures:
    """Le réservoir de la voiture"""
    def __init__(self, marque, capacite, conso):
        self.marque = marque
        self.capacite = capacite  ### Taille du reservoir en litre
        self.conso = conso        ### Litre pour 100 km
        self.carburant = 0
        self.kilometrage = 0


    def faire_le_plein(self,litre):
        place_libre = self.capacite - self.carburant
        self.carburant += min(litre, place_libre)  ###ici on préfère utiliser le 'min' plutot que le 'if'

    def rouler(self,km):
        autonomie = self.carburant / (self.conso * 100)
        if km <= autonomie:
            self.kilometrage += km
            self.carburant -= (km * self.conso) / 100
        else:
            self.kilometrage += autonomie
            self.carburant = 0
            print(f"Panne sèche ! Seulement {autonomie:.0f} km sur {km}.")

    def afficher_etat(self):
        print(f"{self.marque} : {self.carburant:.1f} L, "
              f"{self.kilometrage:.0f} km")



v = Voitures("Toyota", 40, 6)
v.faire_le_plein(30)
v.rouler(200)
v.afficher_etat()
v.rouler(400)             
v.afficher_etat()
v.faire_le_plein(100)     
v.afficher_etat()