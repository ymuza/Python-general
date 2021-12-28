class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    @staticmethod
    def add_course(self, course):
        print(f"enrolled in the {course} course:")


class StudentAthlete(Student):
    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)  # first, last, courses son parametros que recupero de la clase heredada.
        self.sport = sport


courses = ["python", "ruby", "javascript"]
jane = StudentAthlete("jane", "doe", courses, "hockey")
print(jane.sport)
print(isinstance(jane,
                 StudentAthlete))  # metodo para saber si jane pertenece a la clase StudentAthlete. Retorna true si es el caso.
