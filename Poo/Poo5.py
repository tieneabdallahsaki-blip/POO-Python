class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_departement):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_departement = emp_departement

    def calculer_emp_salaire(self, salary, heure_travail):
            heure_sup = 0
            if heure_travail > 50:
                heure_sup = heure_travail - 50
                self.emp_salary = salary + (heure_sup * ( salary / 50 ))

    def emp_affecter_departement(self, emp_departement):
        self.emp_departement = emp_departement

    def afficher_employee(self):
        print(f"ID : {self.emp_id}")
        print(f"Nom : {self.emp_name}")
        print(f"Salaire : {self.emp_salary}")
        print(f"Departement : {self.emp_departement}")
        print("-----------------------------------------")


    

                
emp01 = Employee("E001", "Abdallah", "500000", "Informatique")  
emp02 = Employee("E002", "Saki", "400000", "Finance")
emp03 = Employee("E003", "Tiene", "200000","Vente")

print("_____Detail de l'employee_____")
emp01.afficher_employee()
emp02.afficher_employee()
emp03.afficher_employee()

# Modifier les departements de emp01 et emp03
emp01.emp_affecter_departement("Vente")
emp03.emp_affecter_departement("Informatique")

# Les heures supplementaires des employee
emp01.calculer_emp_salaire(500000, 55)
emp02.calculer_emp_salaire(400000, 64)
emp03.calculer_emp_salaire(200000, 78)

# Les detailles des employees mise à jour
print("_____La mise a jour des employees_____")
emp01.afficher_employee()
emp02.afficher_employee()
emp03.afficher_employee()