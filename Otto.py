import file_handler
import pandas as pd
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
                df = pd.DataFrame(vall,index = range(1,len(vall)+1))
                print(df)
            elif choice == '2':
                ab = 0
                for i in vall:
                    if i['Status'] == 'Available':
                        ab+=1
                        print(i)
                if ab == 0:
                    print('No available valkyries')
            elif choice == '3':
                m =0
                for i in vall:
                    if i['Mission'] != 'None':
                        m+=1
                        print(i)
                if m == 0:
                    print('No valkyries on missions')
            elif choice == '4':
                name = input('Enter the name of the valkyrie: ')
                mission = input('Enter the mission: ')
                for i in vall:
                    if i['Name'] == name:
                        if i['Status'] == 'Injured' or i['Status'] == 'Under medical treatment':
                            print(f'Valkyrie is under medical care.Cannot Assign a mission to {i}')
                        elif i['Status'] =='Deployed':
                            print(f'Valkyrie is already on mission.Cannot Assign a mission to {i}')
                        else:
                            i['Mission'] = mission
                            i['Status'] = 'Deployed'
                            i['ERT'] = 'Not possible'
                            print('Mission assigned successfully!')
                            file_handler.save_data(vall, 'valkyries_database.json')
                        break 
                else:
                    print('Valkyrie not found!Enter valid valkyrie name')
            elif choice == '5':
                rank = input('Enter the rank of the valkyrie: ')
                chi = input('Do you wish to see which valkyries of that rank is availabl?(y/n): ')
                if chi.lower() == 'y':
                    r = 0
                    for i in vall:
                        if i['Rank'] == rank:
                            r+=1
                            print(i)
                    if r == 0: 
                        print('No valkyries of that rank!')
                    print('---------------------------------------')
                    print('available valkyries:')
                    ar = 0
                    for i in vall:
                        if i['Status'] == 'Available' and i['Rank'] == rank:
                            ar +=1
                            print(i)
                    if ar == 0:
                        print('No available valkyries of that rank')
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
                nr = 0
                for i in vall:
                    if i['Name'] == name:
                        nr +=1
                        i['Rank'] = rnk
                        print('Rank promotion successful!')
                        file_handler.save_data(vall, 'valkyries_database.json')
                if nr == 0:
                    print('Valkyrie not found!')
            elif choice == '7':
                print('Exiting...')
                break
            else:
                print('Invalid choice!Choose between 1-7')
    except ValueError:
        print('Invalid choice!Please enter a number')