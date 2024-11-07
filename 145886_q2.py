class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        return f"Grades for {self.name}:\n" + "\n".join(
            f" - {assignment}: {grade}" for assignment, grade in self.assignments.items()
        )


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            return f"No student found with ID {student_id}"

    def display_all_students_grades(self):
        return "\n".join(student.display_grades() for student in self.students)


if __name__ == "__main__":
    instructor = Instructor("Dr. Smith", "Biology 101")
    
    while True:
        print("\nCourse Management System:")
        print("1. Add Student")
        print("2. Assign Grade")
        print("3. Display All Students' Grades")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            student_name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            instructor.add_student(Student(student_name, student_id))
            print(f"{student_name} added to the course.")
        
        elif choice == '2':
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = int(input("Enter grade: "))
            print(instructor.assign_grade(student_id, assignment_name, grade) or "Grade assigned successfully.")
        
        elif choice == '3':
            print(instructor.display_all_students_grades())

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
