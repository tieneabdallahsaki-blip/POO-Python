### Écrivez une classe Python nommée Etudiant 
# avec deux attributs: id_etudiant, nom_etudiant. 
# Créez une fonction display() pour afficher tous 
# les attributs et leurs valeurs dans la classe Etudiant.

class Etudiant:
    id_etudiant = '102'
    nom_etudiant = 'Tiene Saki Abdallah'
    def display():
        print(f"ID de l'etudiant: {Etudiant.id_etudiant}\nNom de l'etudiant: {Etudiant.nom_etudiant}")

print("Attribus et leurs valeurs de la classe etudiant:")
Etudiant.display()
