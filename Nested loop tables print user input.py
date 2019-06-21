input_1 = int(input("\nEnter Starting value of the range :\n---->"))

input_2 = int(input('\nEnter Ending value of the range :\n---->'))

for table_num in range (input_1 , input_2 + 1) :

    print('======================\n\n')
    print('Table of'+ str(table_num ))

    for table in range (1,11) :

        print(table_num , 'x' , str(table) , '=' , str(table_num*table))
