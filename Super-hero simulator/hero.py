''' Objects oriented prograing is when you try to represent key
elment pf software/aplication through objects -- these objecys atre essentially just instances of a blueprint/outline that you create
a class = the blueprint/outline -- this the thing that all our objects are created based off
'''

import random

from pyparsing import Empty


# hero.py

class Hero:
  # We want our hero to have a default "starting_health", so we can set that in the function header.
 
  def __init__(self, name = "hero", starting_health=1000,):
    #Instance properties: name: String, starting_health: Integer current_health: Integer
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors =[]
        self.ability = []
        self.deaths =0
        self.kills = 0
        self.weapons = []
  
  def _repr_(self):
    return f"Hero({self.name})" 

  def add_armors(self, *args):
    new_armors = 0

    for armor in args:

      if armor not in self.armors:
        new_armors += 1
        self.armors.append(armor)

      if new_armors == 1:
        self.armors.append(armor)

    if new_armors == 1:
      message = (f'{self.name} equipped a new piece of armor ')
    
    #else:

  def add_abiility(self, ability):
    self.ability.append(ability)
    return self.ability

  def attack(self):
    attack_value = 0
    for ability in self.ability:
      attack_value+= ability.attack()
    print(f"{self.name} hasb {attack_value} attack")
    return attack_value
 
  def defend(self):
    defend_value = 0
    for armor in self.armor:
      defend_value += armor.defend()

    print(f"{self.name} has {defend_value} defense")
    return defend_value

  def create_hero(self, num):

    hero_name =input (f"\nHero #{num +1}'s name:")
    hero_health = input(f"{hero_name}'s health()Enter a number , try 1000 for default value): ")
    

  
  def add_armor(self,armor):
    self.armor.append(armor)
    return self.armor
   
  def take_damage(self, taking_damage):
    damage = taking_damage - self.defend()
    if damage >0:
      self.current_health -= damage
  
  def add_weapons(self, weapon_damage);
    self.weapons.append(weapon_damage) 
    print(f"{self.nane} weapom has{self.weapons}")

  def battle(self, opponent):
    heroes_names = []

    heroes_names.append(self.name)
    heroes_names.append(opponent.name)

    winner = random.choice (heroes_names)
    loser = []

    for hero in heroes_names:
      if hero != winner:
        loser.append ()

    print(f'{}winner has defeated{loser} ')

    return winner 

  

if __name__ == "__main__":

  hero1 = Hero("Jesus")
  hero2 = Hero("Doodlestain")

  hero1.battle(hero2)

  ability1 = ability("super fast", 100)