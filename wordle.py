# wordle 
import os

word = input('Enter a 5 letter word for the person to guess: ')
while len(word) != 5:
  word = input('The word must be 5 letters: ')
word = word.upper()
os.system('clear')
def wordle(word):
  str = '_____'
  print('You have 5 tries to guess the word! ')
  counter = 0
  guessed_correct = False
  while guessed_correct != True and counter != 5:
    guess = input('Enter a 5 letter word: ')
    if guess == word:
      guessed_correct = True
      break
    while len(guess) != 5:
      guess = input('The guess must be 5 letters: ')
    guess = guess.upper()
    for i in range(0,len(guess)):
      if guess[i] == word[i]:
        str = str[:i] + guess[i] + str[i+1:]
    if str == word:
      print(str)
      guessed_correct = True
      break
    counter += 1
    print(str)
    print(f'You have {5 - counter} tries left')
  if guessed_correct == True:
    a = 'Congrats you guessed the word ' + word + ' correctly!'
    return a
  elif guessed_correct == False:
    a = 'Sorry you ran out of tries, the word was: ' + word
    return a
print(wordle(word))
    
