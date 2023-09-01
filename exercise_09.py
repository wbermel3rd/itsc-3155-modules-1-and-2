#WilliamBermel
#Sources: stackoverflow.com and geeksforgeeks.com

words = []
for x in range(5):
    newWord = input('Enter a word: ')
    words.append(newWord)
sentence = ''
for x in range(len(words)):
    sentence += words[x] + ' '
print('Words: ' + str(words[:]))
print('One String: ' + sentence)