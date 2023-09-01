#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

row = int(input('Enter a row num from 1 to 5: ')) - 1
col = int(input('Enter a col num from 1 to 5: ')) - 1

for x in range(5): 
    for y in range(5): 
        if(x == row and y == col):
            print('1', end=" ")
        else: 
            print('0', end=" ")
        #print('x: ' + str(x) + " y: " + str(y))
    print("")

