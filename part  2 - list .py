# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced with my code solution

# student name: Shashika Rupasinghe
# uow number: w1953826

#Date:   28 November 2022
#Purpose: Anual Student progression
                                      #course work 1, Part 2
#Code

print('\n\t\t\t<<<< Part 2 - List (extension) >>>>\n')

            #variables
count= 1            ##for take the count of credit set
progress_count= 0   ##for take the progress count
trailer_count= 0    ##for take the trailer count
retriever_count= 0  ##for take the retriever count
exclude_count= 0    ##for take the exclude count

            #lists
progress_list= []       ##for store progress credit sets in a list
trailer_list= []        ##for store trailer credit sets in a list
retriever_list= []      ##for store retriever credit sets in a list
exclude_list= []        ##for store exclude credit sets in a list

##create a def to input credit values and check whether it is in range
def value_rule(credit):
    '''
    input credits and check whether is it in range
    '''
    name= credit  ## to keep display message unchange
    while True:
        try:
            credit = int(input(f'please enter your {name:5} credit : '))      ##for get credit
            if credit!= 0 and credit!= 20 and credit!= 40 and credit!= 60 and credit!= 80 and credit!= 100 and credit!= 120:    ##check whether credits are in range
                print(f'Out of range\nEnter a valid {name} credit\n')
                continue
            
        except ValueError:
            print(f'Integer required\nRe-enter {name} credit\n')
            continue
        return credit


##create a def to print histogram
def histogram(credit_type,credit_count):
    '''
    print histogram
    '''
    print(f'{credit_type:10} {str(credit_count):3} : {"*"* int(credit_count)}')


##create a def to print data stored in lists
def input_release(result_name,lists):
    '''
    display the data stored in lists
    '''
    input_count= 1  ## count outputs
    start= 0
    over= 3
    while input_count <= len(lists)/3:      ## loop untile list end
        mark_list = str(lists[start:over])
        mark_list = mark_list.replace('[','').replace(']','')
        release_inputs= print(f'{result_name:26} - {mark_list}')
        start += 3
        over += 3
        input_count += 1
    
        
while True:
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
            progress_list.append(pass_credit)
            progress_list.append(defer_credit)
            progress_list.append(fail_credit)

        elif pass_credit== 100:                                 #rule 2, 3
            print('Progress(module trailer)\n')
            trailer_count += 1
            trailer_list.append(pass_credit)
            trailer_list.append(defer_credit)
            trailer_list.append(fail_credit)

        elif fail_credit <= 60:                                 #rule 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25
            print('Do not progress-module retriever\n')
            retriever_count += 1
            retriever_list.append(pass_credit)
            retriever_list.append(defer_credit)
            retriever_list.append(fail_credit)

        elif fail_credit >= 80:                                 #rule 15, 20, 21, 26, 27, 28
            print('Exclude\n')
            exclude_count += 1
            exclude_list.append(pass_credit)
            exclude_list.append(defer_credit)
            exclude_list.append(fail_credit)

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
            
            input_release('Progress',progress_list)
            input_release('Progress (module trailer)',trailer_list)
            input_release('Module retriever',retriever_list)
            input_release('Exclude',exclude_list)
            
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

