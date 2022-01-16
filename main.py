from random import randint
answer=randint(1,100)

levels_options=['h','e']
lvl=None

while not lvl in levels_options:
  lvl=input('Let\'s guess the number! \nPlease choose a level of difficulty "e" for easy or "h" for hard.').lower()
  print(3)
# if lvl==