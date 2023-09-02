userIn = input('Enter a string: ')
lower = ''
upper = ''
for x in userIn:
    if(x != ' '  and x.isupper()):
        upper += x
    if(x != ' ' and x.islower()):
        lower += x
print(lower + upper)

