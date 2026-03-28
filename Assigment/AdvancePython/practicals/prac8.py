#Write a program to implement different types of inheritance in python

# -------------------------------------
# 1. SINGLE INHERITANCE
# -------------------------------------

class Employee:
    def show_employee(self):
        print("Employee works in the company")

class Developer(Employee):
    def show_developer(self):
        print("Developer writes code")

print("----- Single Inheritance -----")
dev = Developer()
dev.show_employee()
dev.show_developer()


# -------------------------------------
# 2. MULTILEVEL INHERITANCE
# -------------------------------------

class Person:
    def show_person(self):
        print("Person has name and age")

class Employee2(Person):
    def show_employee(self):
        print("Employee works in company")

class Manager(Employee2):
    def show_manager(self):
        print("Manager manages team")

print("\n----- Multilevel Inheritance -----")
mgr = Manager()
mgr.show_person()
mgr.show_employee()
mgr.show_manager()


# -------------------------------------
# 3. MULTIPLE INHERITANCE
# -------------------------------------

class Skill:
    def show_skill(self):
        print("Has technical skills")

class Experience:
    def show_experience(self):
        print("Has work experience")

class TeamLead(Skill, Experience):
    def show_role(self):
        print("TeamLead handles project")

print("\n----- Multiple Inheritance -----")
lead = TeamLead()
lead.show_skill()
lead.show_experience()
lead.show_role()