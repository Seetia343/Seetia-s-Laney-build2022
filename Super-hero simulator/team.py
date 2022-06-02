import random 

class Team: 
    def _init_(self, name):
        self.name = name
        self.heroes = []
        self.death = 0
        self.kills = 0

    def add_hero(self, hero):
        self.heroes.append(hero)
        return self.heroes
    

    def remove_hero(self, hero):
        self.heroes.remove(hero)
        return self.heroes

    def view_all_heroes(self):
        for item in self.heroes:
            print(F"this is my team{item.name}")

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.death += 1


    def team attack()