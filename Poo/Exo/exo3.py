class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        if solde_initial < 0:
            raise ValueError("Impossible !")
        self.__solde = solde_initial
        self.__historique = []

    @property
    def solde(self):
        return f"Le solde de {self.titulaire} est de {self.__solde} €co"

    def deposer(self, montant):
        if montant < 0:
            raise ValueError("Impossible de deposer un montant négatif !")
        self.__solde += montant
        self.__historique.append(f"dépôt {montant}")

    def retirer(self, montant):
        if montant < 0:
            raise ValueError("Impossible !")
        if montant > self.__solde:
            raise ValueError("Impossible de retier un montant suppérieur eu solde !")
        self.__solde -= montant
        self.__historique.append(f"retrait {montant}")

    def afficher_historique(self):
       print(f"Historique de {self.titulaire}")
       for operation in self.__historique:
           print(" -", operation)


c1 = CompteBancaire("Awa", 1000)
c2 = CompteBancaire("Tiene", 50000)
c1.deposer(500)
c2.retirer(2000)
c1.retirer(200)
c1.retirer(800)
print("-_-_-_-_-_Historique-_-_-_-_-_")
c1.afficher_historique()
print("")
c2.afficher_historique()
print("")
print("-_-_-_-_-_Solde-_-_-_-_-_")
print(c1.solde)
print("")
print(c2.solde)
