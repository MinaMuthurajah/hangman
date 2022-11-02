word_list = ['mangoes','pineapples','peaches','oranges','strawberries']
print(word_list)

import random
random.choice(word_list)
word = random.choice(word_list)
print(word)
print (random.choice(word_list))

input ('Please enter a single letter:')
guess = input ('Please enter a single letter:')
if len(guess) == 1 and guess.isalpha():0
    print ('good guess!')
else:
    print ('Oops! That is not a valid input')