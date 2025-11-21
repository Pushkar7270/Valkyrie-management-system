import todo_manager
import grade_manager

def main():
    print("Welcome to the School Management System!")
    while True:
        print('-------------------------------------------')
        print("\nPlease select an option:")
        print("1. Manage To-Do List")
        print("2. Manage Grades")
        print("3. Exit")
        print('-------------------------------------------')
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                todo_manager.todo()
            elif choice == 2:
                grade_manager.grade()
            elif choice == 3:
                print("Thank you for using the task manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")
if __name__ == "__main__":
    main()