#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

lists = []
letters = []
userIn = input('Enter a string: ')
for x in range(len(userIn)):
    letters.append(userIn[x])
    if(len(letters) == 3 or (x == len(userIn) - 1)):
        lists.append(letters)
        letters = []
print(str(lists[:]))
