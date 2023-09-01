running = True
nums = []
eNums = []
#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

while(running):
    userIn = input("Enter a number or enter QUIT to quit: ")
    if userIn.isnumeric and userIn != 'QUIT':
        nums.append(int(userIn))
    else: 
        if userIn == 'QUIT':
            running = False

for x in range(len(nums)):
    if nums[x]%2 == 0:
        eNums.append(nums[x])

print('All nums: ' + str(nums[:]))
print('Even nums: ' + str(eNums[:]))