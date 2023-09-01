#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

num = int(input('Enter a number: '))
list = []
average = 0.0
temp = 0.0
for x in range(1, num + 1):
    temp = float(input('Enter number ' + str(x) + ': '))
    average += temp
    list.append(temp)

average /= num
print('List: ' + str(list[:]))
print('Average: ' + str(average))
