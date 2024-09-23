class StudentManager:
    def __init__(self):
        """Initializes the StudentManager with an empty list of students."""
        self.students = []

    def add_student(self, name, grade):
        """Adds a new student with their grade to the list."""
        student = {"name":name, "grade":grade}
        self.students.append(student)
        pass

    def remove_student(self, name):
        """Removes a student from the list by their name."""
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                print("Estudiante eliminado.")
                return
        print(f"Estudiante {name} no encontrado para borrar.")

    def update_grade(self, name, new_grade):
        """Updates the grade of an existing student."""
        for student in self.students:
            if student["name"] == name:
                student["grade"] = new_grade
                return
        print("Estudiante no encontrado para actualizar")
        pass

    def show_students(self):
        """Shows the list of all students with their grades."""
        for student in self.students:
            print(str(student["name"])+" "+str(student["grade"]))
        pass

    def search_grade(self, name):
        """Searches and shows the grade of a student by their name."""
        for student in self.students:
            if student["name"] == name:
                print(student["grade"])
                return
        print("No encontrado")
        pass

# Example usage of the StudentManager class
if __name__ == "__main__":
    manager = StudentManager()
    # Example calls to methods (to be implemented)
    manager.add_student("Ana", 85)
    manager.add_student("Luis", 90)
    manager.show_students()
    manager.update_grade("Ana", 88)
    manager.search_grade("Luis")
    manager.remove_student("Luis")
    manager.show_students()
