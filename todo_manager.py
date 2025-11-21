import File_handler
def todo():
    try:
        Task = File_handler.load_data("tasks.json")
        while True:
            print('---------------------------------')
            print("1. Add task")
            print("2. View tasks")
            print("3. Mark task as completed")
            print("4. Remove task")
            print("5. Exit")
            print('---------------------------------')
            choice = int(input("Enter your choice: "))
            if choice == 1:
                adtsk = input('Add your task please!: ')
                task_dic = {'Task':adtsk,'Status':'Not Done'} 
                Task.append(task_dic)
                File_handler.save_data(Task, "tasks.json")           
                print('your task has been added successfully!')
            elif choice == 2:
                print(Task)
            elif choice == 3:
                print(Task)
                while True:
                    print('Which task do you want to mark as completed?,insert the number of the task you wish to mark.')
                    mark = input('Enter the task number.You can leave by pressing e: ')
                    if mark.lower() == 'e':
                        break
                    try:
                        mark = int(mark)
                        if mark < 1 or mark > len(Task):
                            print('Invalid task number. Please try again.')
                            continue
                        Task[mark - 1]['Status'] = 'Done'
                        print('Task marked as completed successfully!')
                        File_handler.save_data(Task, "tasks.json")
                    except ValueError:
                        print('Invalid input! Please put a number or press e to exit.')
            elif choice == 4:
                print(Task)
                while True:
                    print('Which task do you want to remove?,insert the number of the task you wish to remove.')
                    mark = input('Enter the task number.You can leave by pressing e: ')
                    if mark.lower() == 'e':
                        break
                    try:
                        mark = int(mark)
                        if mark < 1 or mark > len(Task):
                            print('Invalid task number. Please try again.')
                            continue
                        Task.pop(mark - 1)
                        File_handler.save_data(Task, "tasks.json")
                    except ValueError:
                        print('Invalid input! Please put a number or press e to exit.')
            elif choice == 5:
                print('Thank you for using our service!')
                break
            else:
                print('Invalid choice. Please choose  from 1-5.')
    except ValueError:
        print('Invalid input! Please put a number.')
    
