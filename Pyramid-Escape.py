
# Classes

class Hero:

    def __init__(self, name = "Dave", health = 250, health_regen = 0, strength = 40, spellpower = 0, defence = 20):
        self.name = name
        self.health = health
        self.health_regen = health_regen
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence
    
    def __repr__(self):
        return self.name, self.health, self.strength, self.spellpower, self.defence
    
    def lose_health(self, amount):
        self.health = self.health - (amount - self.defence)
        print("{name} has {health} health remaining".format(name = self.name, health = self.health))
    
    def regen_health(self):
        if self.health <= 250:
            self.health += self.health_regen
            print("{name} now has {health} after regenerating {regen} health".format(name = self.name, health = self.health, regen = self.health_regen))

    def attack(self, enemy):
        if self.strength <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.strength - enemy.defence
            print("{name} attacks {enemy} for {damage} damage!".format(name = self.name, enemy = enemy.name, damage = damage_dealt))
            enemy.lose_health(self.strength)
        
        if enemy.health <= 0:
            print("{enemy} has been defeated! Well done!".format(enemy = enemy.name))
    
    def cast_spell(self, enemy):#
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((enemy.defence * 3)/4)
            print("{name}'s spell hits {enemy} for {damage} damage!".format(name = self.name, enemy = enemy.name, damage = damage_dealt))
            enemy.lose_health(self.spellpower)
        
        if enemy.health <= 0:
            print("{enemy} has been defeated! Well done!".format(enemy = enemy.name))

# hero = Hero()
# print(hero.__repr__())


class Enemy:
    
    def __init__(self, name, health, strength, spellpower, defence):
        self.name = name
        self.health = health
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence

    def __repr__(self):
        return self.name, self.health, self.strength, self.spellpower, self.defence
    
    def lose_health(self, amount):
        self.health = self.health - (amount - self.defence)
        print("{name} has {health} health remaining".format(name = self.name, health = self.health))

    def attack(self, hero):
        if self.strength <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.strength - hero.defence
            print("{name} attacks {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.strength)
        
        if hero.health <= 0:
            print("{hero} has been defeated! Try again?".format(hero = hero.name))
    
    def cast_spell(self, hero):
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((hero.defence * 3)/4)
            print("{name}'s spell hits {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.spellpower)
        
        if hero.health <= 0:
            print("{hero} has been defeated! Try again?".format(hero = hero.name))

class Boss:
    def __init__(self, name = "Jack", health = 300, health_regen = 10, strength = 30, spellpower = 60, defence = 50):
        self.name = name
        self.health = health
        self.health_regen = health_regen
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence

    def __repr__(self):
        return self.name, self.health, self.health_regen, self.strength, self.spellpower, self.defence
    
    def lose_health(self, amount):
        self.health = self.health - (amount - self.defence)
        print("{name} has {health} health remaining".format(name = self.name, health = self.health))
    
    def regen_health(self):
        if self.health <= 290:
            self.health += self.health_regen
            print("{name} now has {health} after regenerating {regen} health".format(name = self.name, health = self.health, regen = self.health_regen))

    def attack(self, hero):
        if self.strength <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.strength - hero.defence
            print("{name} attacks {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.strength)
        
        if hero.health <= 0:
            print("{hero} has been defeated! Try again?".format(hero = hero.name))
    
    def cast_spell(self, hero):
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((hero.defence * 3)/4)
            print("{name}'s spell hits {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.spellpower)
        
        if hero.health <= 0:
            print("{hero} has been defeated! Try again?".format(hero = hero.name))


# Loot choice of item after defeating each enemy that gives certain stats
class Item:
    
    def __init__(self, name, health = 0, health_regen = 0, strength = 0, spellpower = 0, defence = 0):
        self.name = name
        self.health = health
        self.health_regen = health_regen
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence
    
    def __repr__(self):
        return self.name, self.health, self.health_regen, self.strength, self.spellpower, self.defence

# hero = Hero()
# enemy = Enemy("John", 200, 50, 0, 20)

# hero.attack(enemy)
# enemy.attack(hero)

# hero.cast_spell(enemy)
# enemy.cast_spell(hero)

# boss = Boss()
# boss.regen_health()