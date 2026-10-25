class CompteBancaire:
    def __init__(self, numero_compte, proprietaire, solde):
        if solde < 0:
            raise ValueError("Le solde ne peut pas être negatif")
        self.numero_compte = numero_compte
        self.proprietaire = proprietaire
        self.solde = solde

    def deposer(self, montant):
        if montant < 0:
            raise ValueError("Le montant ne peut pas être negatif")
        self.solde += montant
        print(f"{montant} €co a ete deposé sur votre compte")
        print()

    def retirer(self, montant):
        if montant < 0:
            raise ValueError("Le montant ne peut pas être negatif")
        if montant > self.solde:
            print("Solde Isuffisant")
            print()
        else:
            self.solde -= montant
            print(f"{montant} €co a ete retiré de votre compte")
            print()

    def afficher_solde(self):
        print(f"Mr/Mme {self.proprietaire}\nVotre solde est de {self.solde} €co")
        print()

    def __str__(self):
        return f"Numero de compte: {self.numero_compte}\nNom: {self.proprietaire}\nSolde: {self.solde} €co"
    

compte01 = CompteBancaire("C001", "Abdallah", 276000000)
compte02 = CompteBancaire("C002", "Tiene", 26500000)
compte03 = CompteBancaire("C003", "Saki", 15000000)

print("__________Details des clients__________")
print(compte01.__str__())
print("------------------------------------------")
print(compte02.__str__())
print("------------------------------------------")
print(compte03.__str__())
print("------------------------------------------")

### les differentes transactions
compte03.retirer(10000000)
compte01.retirer(6500000)
compte02.deposer(15000000)
compte03.retirer(20000000)
compte01.afficher_solde()
compte02.afficher_solde()
compte03.afficher_solde()