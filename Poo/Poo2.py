### Écrivez un programme Python pour créer deux 
# classes vides, Etudiant et Note. Créez maintenant 
# quelques instances et vérifiez si elles sont 
# ou non des instances de ces classes. 
# Vérifiez également si ces classes sont des 
# sous-classes de la classe Object ou non.

class Etudiant:
    pass

class Note:
    pass

etutiant_01 = Etudiant()
note_01 = Note()


print(isinstance(etutiant_01, Etudiant))
print(isinstance(note_01, Etudiant))
print(isinstance(etutiant_01, Note))
print(isinstance(note_01, Note))
print(issubclass(Etudiant, object))
print(issubclass(Note, object))
