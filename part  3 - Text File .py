# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced with my code solution

# student name: Shashika Rupasinghe
# uow number: w1953826

#Date:   5 December 2022
#Purpose: Anual Student progression
                                      #course work 1, Part 3
#Code

print('\n\t\t\t<<<< Part 3 - Text File >>>>\n')

        #variables
count= 1            ##for take the count of credit set
progress_count= 0   ##for take the progress count
trailer_count= 0    ##for take the trailer count
retriever_count= 0  ##for take the retriever count
exclude_count= 0    ##for take the exclude count


record_file= open('student_credit_record.txt','w')      ##open 'student_credit_record.txt' in write mode


##create def to input credit values and check whether it is in range
def value_rule(credit):
    '''
    input credits and check whether is it in range
    '''
    name= credit  ## to keep display message unchange
    while True:
        try:
            credit = int(input(f'please enter your {name:5} credit : '))  ##for get credit
            if credit!= 0 and credit!= 20 and credit!= 40 and credit!= 60 and credit!= 80 and credit!= 100 and credit!= 120:    ##check whether credits are in range
                print(f'Out of range\nEnter a valid {name} credit\n')
                continue
            
        except ValueError:
            print(f'Integer required\nRe-enter {name} credit\n')
            continue
        return credit


##create def to print histogram
def histogram(credit_type,credit_count):
    '''
    print histogram
    '''
    print(f'{credit_type:10} {str(credit_count):3} : {"*"* int(credit_count)}')


##create def to store data in file
def file_history(credit_type, save_pass, save_defer, save_fail):
    '''
    store data in a file
    '''
    record_file.write(f'{credit_type:33} - {str(pass_credit):3}, {str(defer_credit):3}, {str(fail_credit):3}\n')
    
        
while True:
    pass_credit  =  value_rule('pass')
    defer_credit =  value_rule('defer')
    fail_credit  =  value_rule('fail')

    total= pass_credit + defer_credit + fail_credit
    if total != 120:            ##check whether credit total equal to 120
        print('Total incorrect\nCheck and re-enter\n')
        continue

    else:
        if pass_credit== 120:                                   #rule 1
            print('Progress\n')
            progress_count += 1
            file_history('progress','pass_credit','defer_credit','fail_credit')

        elif pass_credit== 100:                                 #rule 2, 3
            print('Progress(module trailer)\n')
            trailer_count += 1
            file_history('Progress(module trailer)','pass_credit','defer_credit','fail_credit')

        elif fail_credit <= 60:                                 #rule 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25
            print('Do not progress-module retriever\n')
            retriever_count += 1
            file_history('Do not progress-module retriever','pass_credit','defer_credit','fail_credit')

        elif fail_credit >= 80:                                 #rule 15, 20, 21, 26, 27, 28
            print('Exclude\n')
            exclude_count += 1
            file_history('Exclude','pass_credit','defer_credit','fail_credit')
        
            
    while True:            
        answer = input('Would you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view results: ')     ##ask from user is he going to input another set of data
        answer= answer.lower()

        if answer == 'q':
            record_file.close()         ##close the file from write mode
            print('-'*55)
            print("\nHistogram\n")
            
            histogram('Progress',progress_count)
            histogram('Trailer',trailer_count)
            histogram('Retriever',retriever_count)
            histogram('Exclude',exclude_count)
            
            print(f'\n{str(count)} outcomes in total')
            print('-'*55)

            file_history= open('student_credit_record.txt','r')     ## open the file in read mode
            content= file_history.read()
            print(content)          ## display data stored in file
            file_history.close()    ## close file from read mode
            break
        
        elif answer == 'y':
            print('\n<<< Enter new student credits >>>\n')
            count += 1
            break

        else:   ##if an invalid command inpute for answer by user, then comes here
            print('\nInvalid Command Input!!\nPlease re-enter an valid command\n')
            continue
    if answer== 'y':
        continue

    else:       ##if answer== q, break
        break
