''' Objects oriented prograing is when you try to represent key
elment pf software/aplication through objects -- these objecys atre essentially just instances of a blueprint/outline that you create
a class = the blueprint/outline -- this the thing that all our objects are created based off
'''

import random

# hero.py

class Hero:
  '''We want our hero to have a default "starting_health",
  so we can set that in the function header.
 
    any class that you create will consist of two parts: you willhave a constructo/ initializer and then you have methods

    there are two important things to take away from the constructor: the first is that you will allow creat your 
    attribute withing the constructor -- attrivutes are the descriptive things about an object or nouns in the simpes term,
    the second is the self parameter
  '''
  
  def __init__(self, name = "Seetia", starting_health=100,):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''
   # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
   
    def battle(self, opponent):

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  my_hero = Hero("Seetia", 200)
  print(my_hero.name)
  print(my_hero.current_health)
    

#  Super_Seetia = Hero("Seetia", 500)
 # print(Super_Seetia.starting_health)