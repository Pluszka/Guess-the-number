from random import randint
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

answer=randint(1,100)

levels_options=['h','e']

def game():

  lvl=None
  while not lvl in levels_options:
    clearConsole()
    lvl=input('Let\'s guess the number! \nPlease choose a level of difficulty "e" for easy or "h" for hard.').lower()

  if lvl=='e':
    attemps=5
  else:
    attemps=10
  print(f'You have {attemps}, gl <3')

  for guess_attemps in range(attemps):
    guess=int(input('Type your guess: '))
    if guess==answer:
      print('You guessed!')
      break
    elif guess<answer:
      print('Too low.')
    else:
      print('Too high.')

  print(f'The answer was {answer}')
  new_game=input('Will you play again? (Y for yes/ anything for no)').upper()
  if new_game=="Y":
    game()

game()
