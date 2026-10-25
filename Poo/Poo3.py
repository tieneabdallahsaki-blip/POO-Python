###crivez une classe Python nommée Etudiant 
# avec deux attributs nom_etudiant, notes. 
# Modifiez les valeurs des attributs de cette 
# classe et affichez les valeurs originales et 
# modifiées de ces attributs.


class Etudiant:
    nom_etudiant = "Tiene Saki Abdallah"
    notes = "213"

print(Etudiant.nom_etudiant)
print(Etudiant.notes)

Etudiant.nom_etudiant = "Abdallah Tiene"
Etudiant.notes = "231"
print(Etudiant.nom_etudiant)
print(Etudiant.notes)


