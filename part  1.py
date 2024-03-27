# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced with my code solution

# student name: Shashika Rupasinghe
# uow number: w1953826

# Date:   19 November 2022
# Purpose: Anual Student progression
                                      #course work 1, Part 1
#Code

print('\n\t\t\t<<<< Part 1 >>>>\n')

##variables
count= 1            ##for take the count of credit set
progress_count= 0   ##for take the progress count
trailer_count= 0    ##for take the trailer count
retriever_count= 0  ##for take the retriever count
exclude_count= 0    ##for take the exclude count

##create def to input credit values and check whether it is in range
def value_rule(credit):
    '''
    input credits and check whether it is in range
    '''
    name= credit  ## to keep display message unchange
    while True:
        try:
            credit = int(input(f'please enter your {name:5} credit : '))        ##for get credit
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


print('\t\tWelcome!\n')
while True:
    try:
        print('\tWhat is your position?\n\'1\' - Student\n\'2\' - Staff member\n\'3\' - Exit\n') ##ask from user he want to use program in student mode or teacher mode
        mode_select= int(input('Enter your answer: '))
        print('')
        if mode_select== 1:
            pass_credit  =  value_rule('pass')
            defer_credit =  value_rule('defer')
            fail_credit  =  value_rule('fail')

            total= pass_credit + defer_credit + fail_credit
            if total != 120:            ##check whether credit total equal to 120
                print('Total incorrect\nPlease check and re-enter\n')
                continue

            else:
                if pass_credit== 120:                                   #rule 1
                    print('Progress\n')

                elif pass_credit== 100:                                 #rule 2, 3
                    print('Progress(module trailer)\n')

                elif fail_credit <= 60:                                 #rule 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25
                    print('Do not progress-module retriever\n')

                elif fail_credit >= 80:                                 #rule 15, 20, 21, 26, 27, 28
                    print('Exclude\n')
                continue

        ##if mode_select != 1 then comes to this              
        elif mode_select== 2:
            
            while True:
                print('')
                pass_credit  =  value_rule('pass')
                defer_credit =  value_rule('defer')
                fail_credit  =  value_rule('fail')

                total= pass_credit + defer_credit + fail_credit
                if total != 120:            ##check whether credit total equal to 120
                    print('Total incorrect\nPlease check and re-enter\n')
                    continue

                else:
                    if pass_credit== 120:                                   #rule 1
                        print('Progress\n')
                        progress_count += 1

                    elif pass_credit== 100:                                 #rule 2, 3
                        print('Progress(module trailer)\n')
                        trailer_count += 1

                    elif fail_credit <= 60:                                 #rule 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25
                        print('Do not progress-module retriever\n')
                        retriever_count += 1

                    elif fail_credit >= 80:                                 #rule 15, 20, 21, 26, 27, 28
                        print('Exclude\n')
                        exclude_count += 1
                        
                        
                while True:
                    answer = input('Would you like to enter another set of data?\nEnter \'y\' for yes or \'q\' to quit and view results: ')     ## ask from user is he going to input another set of data
                    answer= answer.lower()

                    if answer == 'q':
                        print('-'*55)
                        print("\nHistogram\n")
                        
                        histogram('Progress',progress_count)
                        histogram('Trailer',trailer_count)
                        histogram('Retriever',retriever_count)
                        histogram('Exclude',exclude_count)
                        
                        print(f'\n{str(count)} outcomes in total')
                        print('-'*55)
                        break
                    
                    elif answer == 'y':
                        print('\n<<< Enter new student credits >>>\n')
                        count += 1
                        break

                    else:   ##if an invalid command inpute for answer by user, then comes here
                        print('\nInvalid Command Input!!\nPlease re-enter a valid command\n')
                        continue
                if answer== 'y':
                    continue
                
                else:       ##if answer== q, break
                    break
            if answer== 'q':
                continue
        elif mode_select== 3:
            print('exit')
            break
        
        ## if mode_select != 1 or 2 or 3then come to this part
        else:
            print('invalid mode\n')

    ##if an integer not entered to mode_select then comes here
    except ValueError:
        print("integer '1' or '2' required\n")
