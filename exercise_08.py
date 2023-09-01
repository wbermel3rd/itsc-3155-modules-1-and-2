#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

orig = []
unique = []
for x in range(1, 11):
    userIn = input('Enter number ' + str(x) + ': ')
    orig.append(int(userIn))
for x in range(len(orig)):
    if not unique.__contains__(orig[x]):
        unique.append(orig[x])
print('Original List: ' + str(orig[:]))
print('Nums that appear once: ' + str(unique[:]))