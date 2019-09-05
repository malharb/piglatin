# pig latin. by malhar bhide

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        print(word + 'ay')

    else:
        print(word[1:] + first_letter + 'ay')

word = input('Enter any word: ')
pig_latin(word)

input('Press ENTER to exit')
