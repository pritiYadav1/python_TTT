class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, grade):
        if student_id not in self.students:
            self.students[student_id] = {'Name': name, 'Grade': grade}
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists. Please choose a different ID.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student ID not found.")

    def display_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("Student Management System:")
            print("---------------------------")
            for student_id, details in self.students.items():
                print(f"ID: {student_id}, Name: {details['Name']}, Grade: {details['Grade']}")
            print("---------------------------")

# Example usage:
if __name__ == "__main__":
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            sms.add_student(student_id, name, grade)

        elif choice == '2':
            student_id = input("Enter Student ID to remove: ")
            sms.remove_student(student_id)

        elif choice == '3':
            sms.display_students()

        elif choice == '4':
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
