import time 
import file_handler
def valk():
    valks = file_handler.load_data('valkyries_database.json')
    try:
        while True:
            print('------------------------------------------')
            print('Welcome Amber')
            print('What would you like to do?')
            print('1. Add a Valkyrie')
            print('2. View all free Valkyries')
            print('3. View Valkyries that are on mission')
            print('4. View all valkyries')
            print('5. Assign valkyrie for medical treatment')
            print('6. Update availability of the valkyrie')
            print('7. Update ERT of the valkyrie')
            print('8. Update estimated mission time(EMT)')
            print('9. Exit')
            print('------------------------------------------')
            choice = input('Enter your choice: ')
            if choice == '1':
                name = input('Enter the name of the Valkyrie you want to add: ')
                if name.isdigit():
                    print('invalid valkyrie name!')
                    continue
                rank = input('Enter the rank of the Valkyrie: ')
                if rank.isdigit():
                    print('invalid rank!')
                    continue
                Branch = input('Enter the assigned branch of the valkyrie: ')
                if Branch.isdigit():
                    print('invalid branch name!')
                    continue
                vlk = {'Name':name, 'Rank':rank, 'Branch':Branch,'Status':'Available','Mission':'None','ERT':'24 hours','EMT': 'None'}
                valks.append(vlk)
                print('Valkyrie added successfully!')
                file_handler.save_data(valks,'valkyries_database.json')
            elif choice =='2':
                for i in valks:
                    if i['Status'] == 'Available':
                        print(i)
                    else:
                        print('No Valkyries are available')
                        continue
                    if valks == []:
                        print('Database is empty')
            elif choice == '3':
                for i in valks:
                    if i['Mission'] != 'None':
                        print(i)
                    elif valks == []:
                        print('Database is empty')
            elif choice =='4':
                print(valks)
                if valks == []:
                    print('Database is empty')
            elif choice =='5':
                for i in valks:
                    if i['Status'] == 'Injured':
                        print(f'Below valkyries need medical treatment ASAP!: {i}')
                        choice2 = input('Send them for medical treatment?(Y/N): ')
                        if choice2.lower() == 'y':
                            i['Status'] = 'Under medical treatment'
                            file_handler.save_data(valks, 'valkyries_database.json')
                            print('Successfully sent valkyrie for treatment!')
                        elif choice2.lower() == 'n':
                            continue
                        else:
                            print('Invalid choice')
                    elif valks == []:
                        print('Database is empty')
            elif choice == '6':
                vlk1 = input('Enter the name of the valkyrie: ')
                avail = input('Enter the new status: ')
                if i['Name'] == vlk1:
                    i['Status'] == avail
                    print('Status updated successfully')
                    file_handler.save_data(valks, 'valkyries_database.json')
                elif valks == []:
                    print('Database is empty')
                elif vlk1.isdigit() or avail.isdigit():
                    print('invalid valkyrie name!')
                    continue
            elif choice == '7':
                valk2 = input('Enter the name of the valkyrie.')
                Ert = input('Enter the new ERT: ')
                for i in valks:
                    if i['Name'] == valk2:
                        i['ERT'] = Ert
                        print('ERT updated successfully')
                        file_handler.save_data(valks, 'valkyries_database.json')
                    elif i['Name'] != valk2:
                        print('Valkyrie not found!')
                    else:
                        print('Write valid valkyrie name please!')
            elif choice == '8':
                char = input('Enter the name of the valkyrie: ')
                emt = input('Enter the new EMT: ')
                for i in valks:
                    if i['Name'] == char:
                        i['EMT'] == emt
                        print('Estimated mission Time updated successfully')
                        file_handler.save_data(valks,'valkyries_database.json')
                    elif valks == []:
                        print('Database is empty')
            elif choice == '9':
                print('Exiting...')
                time.sleep(1)   
                break
            else:
                print('Invalid choice.Choose number between 1-9')
    except ValueError:
        print('Invalid choice')

