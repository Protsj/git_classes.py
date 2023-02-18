class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Hi, {self.name} {self.surname}.'

    def __repr__(self):
        return f'{self.name} {self.surname}'

class Student(Person):
    def __init__(self, name, surname, crs, prof):
        self.crs = int(crs)
        self.prof = prof
        super().__init__(name, surname)

    def __str__(self):
        return f'{self.name} {self.surname}, you are on a {self.crs} course.' \
               f' Your profession is {self.prof}.)'

    def __repr__(self):
        return f'{self.name}, {self.surname}, {self.crs}, {self.prof}'

class Professor(Person):
    def __init__(self, name, surname, exp, subj):
        self.exp = exp
        self.subj = subj
        super().__init__(name, surname)

    def __str__(self):
        return f'{self.name} {self.surname} have been teaching {self.subj} for {self.exp}.'

    def __repr__(self):
        return f'{self.subj}, {self.exp}'

class University(Student):
    def __init__(self, name, surname, crs, prof, university_name, budget):
        self.university_name = university_name
        self.budget = int(budget)
        super().__init__(name, surname, crs, prof)

    def check_budget(self):
        try:
            money_spent = self.budget * self.crs
            return f'{self.university_name} spent {money_spent}$ on {self.name} {self.surname}.'
        except Exception:
            return f'Error, sorry...'

    def __str__(self):
        return f'{self.name}, {self.surname} is in the {self.university_name}. They give the best students {self.budget}$.'

    def __repr__(self):
        return f'{self.name}, {self.surname}, {self.university_name}, {self.budget}'


amyh = University('Amy', 'Hinderson', 17, 'Mathematics', 'Oxford', 3000)
print(amyh)
print(amyh.check_budget())