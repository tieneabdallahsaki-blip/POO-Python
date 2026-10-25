class BankAccont:
    def __init__(self,numero_compte, solde, date_ouverture, nom_du_client):
        self.numero_compte = numero_compte
        self.solde = solde
        self.date_ouverture = date_ouverture
        self.nom_du_client = nom_du_client

    def versement(self, nouveau_solde):
        self.solde += nouveau_solde
        print(f"Votre nouveau solde est: {self.solde} Eco")
        print("-------------------------------------------")

    def retrait(self, nouveau_solde):
        if nouveau_solde > self.solde:
            print("Solde insuffisant")
            print("-------------------------------------------")
        else:
            self.solde -= nouveau_solde
            print(f"{nouveau_solde} Eco a ete retiré de votre compte")
            print(f"Votre nouveau solde est de {self.solde} Eco")
            print("-------------------------------------------")

    def verification_solde(self):
        print(f"Mr/Mm {self.nom_du_client}\nVotre solde actuelle est de {self.solde} Eco")
        print("-------------------------------------------")

    def info_client(self):
        print(f"Numero de compte: {self.numero_compte}")
        print(f"Date d'ouverture: {self.date_ouverture}")
        print(f"Nom du client: {self.nom_du_client}")
        print(f"Solde: {self.solde} Eco")
        print("-------------------------------------------")

client01 = BankAccont("C27102", 25000000, "13-02-2027", "Tiene Saki Abdallah")
client02 = BankAccont("C29102", 22000000, "01-10-2022", "Jean DeLaroche")
client03 = BankAccont("C17029", 18000000, "09-05-2019", "Kouassi Konan")

print(f"----------Information du client----------")
client01.info_client()
client02.info_client()
client03.info_client()

print("-_-_-_-_-_Transactions_-_-_-_-_-")
client03.versement(2000000)
client03.retrait(20500000)
client03.retrait(500000)
client03.retrait(1000000)
client03.verification_solde()
