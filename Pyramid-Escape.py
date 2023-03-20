
# Classes

class Hero:

    def __init__(self, name = "Dave", health = 250, strength = 40, spellpower = 0, defence = 20):
        self.name = name
        self.health = health
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence
    
    def __repr__(self):
        return self.name, self.health, self.strength, self.spellpower, self.defence




hero = Hero()
print(hero.__repr__())