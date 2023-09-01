#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

num = int(input('Enter a grade from 0 to 100: '))
if(num < 60):
    print('Your grade is F')
elif(num < 70 and num >= 60):
    print('Your grade is D')
elif(num < 80 and num >= 70):
    print('Your grade is C')
elif(num < 90 and num >= 80):
    print('Your grade is B')
elif(num <= 100 and num >= 90):
    print('Your grade is A')
else:
    print('Invalid input.')