class Etudiant:
    def __init__(self, nom, numero_matricule, notes01, notes02):
        self.nom = nom
        self.numero_matricule = numero_matricule
        self.notes01 = notes01
        self.notes02 = notes02

    def accepter(self, nom, numero_matricule, notes01, notes02):
        e = Etudiant(nom, numero_matricule, notes01, notes02)
        self.etudiants.append(e)

    def display(self):
        print(f"Nom: {self.e.nom}")
        print(f"Matricule: {self.e.numero_matricule}")
        print(f"Note 01: {self.e.notes01}")
        print(f"Note 02: {self.e.notes02}")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    
        