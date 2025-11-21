import File_handler
def grade():
    marks = File_handler.load_data("marks.json")
    while True:
        try:
            print('---------------------------------')
            print("1. Enter marks")
            print("2. View marks")
            print("3. Change marks")
            print("5. Exit")                 
            print('---------------------------------')
            choice = int(input("Enter your choice: "))
            if choice == 1:                                                                        #choice 1
                while True:
                    subject = input('Enter the subject, or press e to exit: ')
                    if subject.lower() == 'e':
                        break
                    mark = input('Enter your mark,or press e to exit: ')
                    credit = input('Enter the credit or press e to exit: ')
                    if subject.isdigit():
                        print('Invalid subject. Please enter a valid subject.')
                        continue
                    if mark.lower() == 'e' or credit.lower()== 'e':
                        break
                    try:
                        mark = int(mark)
                        if mark < 0 or mark > 100:
                            print('Invalid mark. Please enter a mark between 0 and 100.')
                            continue
                    except ValueError:
                        print('Invalid input! Please put a number or press e to exit.')
                        continue
                    try:
                        credit = float(credit)
                        if credit < 0:
                            print('Invalid credit. Please enter a positive number.')
                            continue
                        elif credit>4:
                            print('Credit cannot be more than 4')
                            continue
                    except ValueError:
                        print('Invalid input! Please put a number or press e to exit.')
                        continue
                    mark_dict = {'Subject': subject, 'Marks': mark , 'Credit':credit}
                    marks.append(mark_dict)
                    File_handler.save_data(marks, "marks.json")
            elif choice == 2:                                                                      #choice 2
                print(marks)
            elif choice == 3:
                print(marks)
                try:
                    sub = input('Enter the subject you want to change: ')
                    mrk = int(input('Enter the new mark: '))
                    crd = float(input('Enter the new credit: '))
                    if sub.isdigit():
                        print('Invalid subject. Please enter a valid subject.')
                        continue
                    elif mrk<0 or mrk>100:
                        print('Invalid mark. Please enter a mark between 0 and 100.')
                        continue
                    elif crd<0 or crd>4:
                        print('Invalid credit. Please enter a valid credit score.')
                    for i in marks:
                        if i['Subject'] == sub:
                            i['Marks'] = mrk
                            i['Credit'] = crd
                            File_handler.save_data(marks, "marks.json")
                            print('Mark changed successfully!')
                            break
                    else:
                        print('Error finding subject! Please enter a valid Subject.')
                except ValueError:
                    print('Invalid input! Please put a number.')
            elif choice == 4:
                if not marks:
                    print("No data found. Please enter marks first.")
                    continue
                total_points = 0
                total_credits = 0                
                for i in marks:
                    mark = float(i['Marks'])
                    credit = float(i['Credit'])
                    grade_point = mark / 10
                    total_points += (grade_point * credit)
                    total_credits += credit
                    print(f"{i['Subject']}: {grade_point} (GP) x {credit} (Cr)")
                if total_credits == 0:
                    print("Total credits is 0. Cannot calculate CGPA.")
                else:
                    cgpa = total_points / total_credits
                    print("------------------------")
                    print(f"Your CGPA is: {cgpa:.2f}") 
                    print("------------------------")
            elif choice == 5:
                break
            else:
                print('Invalid choice. Please choose 1-4.')
        except ValueError:
            print('Invalid input! Please put a number.')
          
