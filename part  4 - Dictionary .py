# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced with my code solution

# student name: Shashika Rupasinghe
# uow number: w1953826

#Date:   9 December 2022
#Purpose: Anual Student progression
                                      #course work 1, Part 4
#Code

print('\n\t\t\t<<<< Part 4 - Dictionary >>>>\n')

student_dict = dict()   ##create a dictionary to store data


##create def to input credit values and check whether it is in range
def value_rule(credit):
    '''
    input credits and check whether is it in range
    '''
    name= credit  ## to keep display message unchange
    while True:
        try:
            credit = int(input(f'please enter your {name:5} credit : '))      ##for get credit
            if credit!= 0 and credit!= 20 and credit!= 40 and credit!= 60 and credit!= 80 and credit!= 100 and credit!= 120:    ##check whether credits are in range
                print(f'Out of range\nEnter valid {name} credit\n')
                continue
            
        except ValueError:
            print(f'Integer required\nRe-enter {name} credit\n')
            continue
        return credit

##create a def to store data in a dictionary
def student_dictionary(student_num, result_type, pass_credit, defer_credit, fail_credit):
    '''
    to store data in a dictionary
    '''
    student_dict[student_num] = {result_type : [pass_credit ,defer_credit ,fail_credit]}


       
while True:
    while True:     ##check whether student number is valid as per valid format
        print('Student number must begin with \'w\' and should have seven numbers')
        student_num= str(input('Enter student number: '))
        print(' ')
        if len(student_num)== 8 and (student_num[0]== 'w' or student_num[0]== 'W'):     ##check the student number
            break       ##if number is correct break
        else:
            print('Wrong student number')
            continue        ##loop until correct student number is input
        
    pass_credit  =  value_rule('pass')
    defer_credit =  value_rule('defer')
    fail_credit  =  value_rule('fail')

    total= pass_credit + defer_credit + fail_credit
    if total != 120:        ##check whether credit total equal to 120
        print('Total incorrect\nCheck and re-enter\n')
        continue

    else:
        if pass_credit== 120:                                   #rule 1
            print('Progress\n')
            student_dictionary(student_num, 'progress', pass_credit, defer_credit, fail_credit)

        elif pass_credit== 100:                                 #rule 2, 3
            print('Progress(module trailer)\n')
            student_dictionary(student_num, 'progress(module trailer)', pass_credit, defer_credit, fail_credit)

        elif fail_credit <= 60:                                 #rule 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25
            print('Do not progress-module retriever\n')
            student_dictionary(student_num, 'module retriever', pass_credit, defer_credit, fail_credit)

        elif fail_credit >= 80:                                 #rule 15, 20, 21, 26, 27, 28
            print('Exclude\n')
            student_dictionary(student_num, 'Exclude', pass_credit, defer_credit, fail_credit)
            
    while True:            
        answer = input('Would you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view results: ')     ## ask from user is he going to input another set of data
        answer= answer.lower()
        print('')

        ##print Dictionary
        if answer == 'q':
            print('\tStudent Data')
            for i in student_dict.keys():
                for r in student_dict[i].keys():
                    mark_str = str(student_dict[i][r]).replace("[", "").replace("]", "")
                    print(f'{i} : {r} - {mark_str}\t',end='')
            break

        elif answer == 'y':
            print('\n<<< Enter new student credits >>>\n')
            break

        else:   ##if an invalid command inpute for answer by user, then comes here
            print('\nInvalid Command Input!!\nPlease re-enter an valid command\n')
            continue
    if answer== 'y':
        continue

    else:       ##if answer== q, break
        break
