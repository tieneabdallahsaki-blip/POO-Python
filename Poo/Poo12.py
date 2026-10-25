class CompteBancaire:
    def __init__(self, numero_compte, proprietaire, solde):
        self.numero_compte = numero_compte
        self.proprietaire = proprietaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"Mr/Mme {self.proprietaire}\n{self.solde} €co a ete deposé sur votre compte.")

    def retirer(self, montant):
        if montant > self.solde:
            print("Solde Inssufisant!!")
        else:
            self.solde -= montant
            print(f"Mr/Mme {self.proprietaire}\n{self.solde} €co a ete retiré de votre compte.")

    def afficher_solde(self):
        print(f"Mr/Mme {self.proprietaire}\nVotre solde est de {self.solde} €co.")

    def __str__(self):
        return f"Numero de compte: {self.numero_compte}\nNom: {self.proprietaire}\nSolde: {self.solde}"


client01 = CompteBancaire("C01", "Abdallah", 50000000)
client02 = CompteBancaire("C02", "Saki", 50000000)
client03 = CompteBancaire("C03", "Tiene", 50000000)
print("-----detail du client-----")
print(client01.__str__())
print("--------------------------")
print(client02.__str__())
print("--------------------------")
print(client03.__str__())
print("--------------------------")

