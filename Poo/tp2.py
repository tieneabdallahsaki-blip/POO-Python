class Livre:
    ### self.disponible = True signifie : au départ, le livre est disponible
    def __init__(self, titre, auteur, isbn, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = disponible

### Si le livre est disponible, on le passe à indisponible.
### Sinon, on retourne False.
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def rendre(self):
        self.disponible = True
        return True


class Bibliotheque:
    ### On crée une liste privée pour stocker tous les livres.
    def __init__(self):
        self.__livres = []

    def ajouter_livre(self, livre):
        self.__livres.append(livre)

    def chercher_par_titre(self, titre):
        return [livre for livre in self.__livres if livre.titre.lower() == titre.lower()]

    def livres_disponibles(self):
        return [livre for livre in self.__livres if livre.disponible]

    def emprunter_livre(self, isbn):
        for livre in self.__livres:
            if livre.isbn == isbn:
                if livre.emprunter():
                    return f"Le livre '{livre.titre}' a été emprunté."
                return f"Le livre '{livre.titre}' est déjà emprunté."
        return "Livre introuvable."
