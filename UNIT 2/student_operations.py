students = []
next_id = 1

def add_student():
    global next_id
    print("\n--- Add Student ---")
    student_name = input("Enter student name: ")
    student_id = f"S{next_id:03d}"
    next_id += 1

    student = {'id': student_id, 'name': student_name}
    students.append(student)
    print(f"Student '{student_name}' with ID '{student_id}' added.")

def search_student():
    print("\n--- Search Student ---")
    if not students:
        print("No students to search.")
        return

    search_term = input("Enter student ID or name to search: ").lower()
    found_students = [s for s in students if search_term in s['id'].lower() or search_term in s['name'].lower()]

    if found_students:
        print("Found Students:")
        for s in found_students:
            print(f"ID: {s['id']}, Name: {s['name']}")
    else:
        print("No student found matching the search term.")

def list_all_students():
    print("\n--- List All Students ---")
    if not students:
        print("No students to display.")
        return

    print("Current Students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}")

def update_student():
    print("\n--- Update Student ---")
    if not students:
        print("No students to update.")
        return

    student_id = input("Enter the ID of the student to update: ")
    found = False
    for s in students:
        if s['id'] == student_id:
            new_name = input(f"Enter new name for student '{s['name']}' (current: {s['name']}): ")
            s['name'] = new_name
            print(f"Student ID '{student_id}' updated to name '{new_name}'.")
            found = True
            break
    if not found:
        print(f"Student with ID '{student_id}' not found.")

def delete_student():
    print("\n--- Delete Student ---")
    if not students:
        print("No students to delete.")
        return

    student_id = input("Enter the ID of the student to delete: ")
    initial_len = len(students)
    global students
    students = [s for s in students if s['id'] != student_id]

    if len(students) < initial_len:
        print(f"Student with ID '{student_id}' deleted.")
    else:
        print(f"Student with ID '{student_id}' not found.")

def main_menu():
    while True:
        print("\n--- Student Operations Menu ---")
        print("a) Add Student")
        print("b) Search Student")
        print("c) List All Students")
        print("d) Update Student")
        print("e) Delete Student")
        print("f) Exit")

        choice = input("Enter your choice (a-f): ").lower()

        if choice == 'a':
            add_student()
        elif choice == 'b':
            search_student()
        elif choice == 'c':
            list_all_students()
        elif choice == 'd':
            update_student()
        elif choice == 'e':
            delete_student()
        elif choice == 'f':
            print("Exiting Student Operations. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a, b, c, d, e, or f.")

if __name__ == "__main__":
    main_menu()
