class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)

    def display_all_employees(self):
        return "\n".join(employee.display_details() for employee in self.employees)


if __name__ == "__main__":
    departments = {}

    while True:
        print("\nEmployee and Department Management System:")
        print("1. Create Department")
        print("2. Add Employee to Department")
        print("3. Update Employee Salary")
        print("4. Display All Employees in a Department")
        print("5. Calculate Total Salary Expenditure for a Department")
        print("6. List All Departments")
        print("7. Calculate Total Salary Expenditure for All Departments")
        print("8. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            dept_name = input("Enter the new department name: ")
            if dept_name in departments:
                print(f"Department '{dept_name}' already exists.")
            else:
                departments[dept_name] = Department(dept_name)
                print(f"Department '{dept_name}' created.")

        elif choice == '2':
            dept_name = input("Enter the department name to add an employee: ")
            if dept_name in departments:
                name = input("Enter employee name: ")
                employee_id = input("Enter employee ID: ")
                salary = float(input("Enter salary: "))
                employee = Employee(name, employee_id, salary)
                departments[dept_name].add_employee(employee)
                print(f"Employee {name} added to department '{dept_name}'.")
            else:
                print(f"Department '{dept_name}' not found. Please create it first.")

        elif choice == '3':
            dept_name = input("Enter the department name to update an employee's salary: ")
            if dept_name in departments:
                employee_id = input("Enter employee ID to update salary: ")
                department = departments[dept_name]
                employee = next((e for e in department.employees if e.employee_id == employee_id), None)
                if employee:
                    new_salary = float(input("Enter new salary: "))
                    employee.update_salary(new_salary)
                    print(f"Salary updated for {employee.name}.")
                else:
                    print("Employee not found.")
            else:
                print(f"Department '{dept_name}' not found.")

        elif choice == '4':
            dept_name = input("Enter the department name to display employees: ")
            if dept_name in departments:
                print(f"Employees in {dept_name} department:")
                print(departments[dept_name].display_all_employees())
            else:
                print(f"Department '{dept_name}' not found.")

        elif choice == '5':
            dept_name = input("Enter the department name to calculate total salary: ")
            if dept_name in departments:
                total_salary = departments[dept_name].calculate_total_salary()
                print(f"Total Salary Expenditure for {dept_name} department: {total_salary}")
            else:
                print(f"Department '{dept_name}' not found.")

        elif choice == '6':
            print("Departments:")
            for dept in departments:
                print(f" - {dept}")

        elif choice == '7':
            total_expenditure = sum(dept.calculate_total_salary() for dept in departments.values())
            print(f"Total Salary Expenditure for All Departments: {total_expenditure}")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
