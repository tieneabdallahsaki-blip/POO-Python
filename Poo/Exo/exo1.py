class Livre:
    def __init__(self,titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def afficher(self):
        print(f"<<{self.titre}>> de {self.auteur} ({self.nb_pages} pages).")

    def estLong(self):
        return self.nb_pages > 300

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre2 = Livre("Les Misérables", "Victor Hugo", 1500)
livre3 = Livre("Une si longue lettre", "Mariama Bâ", 131)

for livre in [ livre1, livre2, livre3 ]:
    livre.afficher()
    print("  Livre long ?", livre.estLong())


### print("-------------AFFICHAGES-------------")
### livre1.afficher()
### livre2.afficher()
### livre3.afficher()

### print("-------------EST LONG-------------")
### print(livre3.estLong())
### print(livre2.estLong())