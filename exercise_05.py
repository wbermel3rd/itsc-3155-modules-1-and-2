#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

l1 = []
l2 = []
l3 = []
for x in range(5):
    l1.append(int(input('Enter a number for the first list: ')))
for x in range(5):
    l2.append(int(input('Enter a number for the second list: ')))
print('List 1: ' + str(l1[:]))
print('List 2: ' + str(l2[:]))

for x in range(len(l1)):
    if l2.__contains__(l1[x]) and not l3.__contains__(l1[x]):
        l3.append(l1[x])

print('List 3: ' + str(l3[:]))


