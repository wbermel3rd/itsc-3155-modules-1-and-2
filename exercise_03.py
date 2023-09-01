#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

num = int(input('Enter an integer greater than 1: '))
if(num <= 1):
    print('Invalid input')
else: 
    for x in range(num+1):
        cubed = (int)(x*x*x)
        print('The cube of ' + str(x) + ' is ' + str(cubed))