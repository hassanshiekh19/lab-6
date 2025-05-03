def print_students_alphabetically(filename):
    try:
        with open(filename, 'r') as file:

            students = [line.strip() for line in file if line.strip()]

            students.sort()

            print("Student names in alphabetical order:")
            for name in students:
                print(name)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print_students_alphabetically("students.txt")
