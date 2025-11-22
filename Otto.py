import file_handler
def otto():
    vall = file_handler.load_data('valkyries_database.json')
    try:
        while True:
            print('-----------------------------------')
            print('Welcome Mr. Otto')
            print('What would you like to do?')
            print('1. View all valkyries')
            print('2. view all available valkyries')
            print('3. View all valkyries on missions')
            print('4. Assign mission to valkyries.')
            print('5. view valkyries of specific rank')
            print('6. Promote a valkyrie.')
            print('7. Exit')
            print('---------------------------------------')
            choice = input('Enter your choice: ')
            if choice == '1':
                print(vall)
            elif choice == '2':
                for i in vall:
                    if i['Status'] == 'Available':
                        print(i)
                    else:
                        print('No valkyries available')
            elif choice == '3':
                for i in vall:
                    if i['Status'] != 'None':
                        print(i)
                    else:
                        print('No valkyries on missions')
            elif choice == '4':
                name = input('Enter the name of the valkyrie: ')
                mission = input('Enter the mission: ')
                for i in vall:
                    if i['Name'] == name:
                        i['Mission'] = mission
                        print('Mission has been assigned.')
                        file_handler.save_data(vall, 'valkyries_database.json')
                    elif i['Name'] != name:
                        print('Valkyrie not found!Enter valid Valkyrie name')
            elif choice == '5':
                rank = input('Enter the rank of the valkyrie: ')
                chi = input('Do you wish to see which valkyries of that rank is availabl?(y/n): ')
                if chi.lower() == 'y':
                    for i in vall:
                        if i['Rank'] == rank:
                            print(i)
                        else: 
                            print('No valkyries of that rank!')
                    print('---------------------------------------')
                    print('available valkyries:')
                    for i in vall:
                        if i['Status'] == 'Available' and i['Rank'] == rank:
                            print(i)
                elif chi.lower() == 'n':
                    for i in vall:
                        if i['Rank'] == rank:
                            print(i)
                else:
                    print('Invalid choice')
                    continue
            elif choice == '6':
                name = input('Enter the name of the valkyrie: ')
                rnk = input('Enter the new rank of the valkyrie: ')
                for i in vall:
                    if i['Name'] == name:
                        i['Rank'] = rnk
                        print('Rank promotion successful!')
                        file_handler.save_data(vall, 'valkyries_database.json')
                    else:
                        print('Valkyrie not found!')
            elif choice == '7':
                print('Exiting...')
                break
            else:
                print('Invalid choice!Choose between 1-7')
    except ValueError:
        print('Invalid choice!Please enter a number')

    
            
