#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

str1 = input('Enter a string: ')
str2 = input('Enter another string: ')
if str1.endswith(str2) or str2.endswith(str1):
    print('True')
else:
    print('False')