
# Classes

class Hero:

    def __init__(self, name = "Dave", health = 250, health_regen = 0, strength = 40, spellpower = 0, defence = 20, health_potion = 2):
        self.name = name
        self.health = health
        self.health_regen = health_regen
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence
        self.health_potion = health_potion
    
    def __repr__(self):
        return self.name, self.health, self.health_regen, self.strength, self.spellpower, self.defence
    
    def lose_health(self, amount):
        self.health = self.health - (amount - self.defence)
        if self.health <= 0:
            self.health = 0
            print("{hero} has been defeated! Try again?".format(hero = self.name))
        else:
            print("{name} has {health} health remaining".format(name = self.name, health = self.health))
    
    def regen_health(self):
        if self.health <= 250:
            self.health += self.health_regen
            print("{name} now has {health} after regenerating {regen} health".format(name = self.name, health = self.health, regen = self.health_regen))

    def use_health_pot(self):
        if self.health == 250:
            print("You are already at full health! No need to use a health potion!")
            print("You have {} health potion(s) remaining".format(self.health_potion))
        elif self.health_potion > 0 and self.health >= 150:
            self.health_potion -= 1
            self.health = 250
            print("Health potion used: You're now max health {health}hp".format(health = self.health))
            print("You have {} health potion(s) remaining".format(self.health_potion))
        elif self.health_potion > 0 and self.health < 150:
            self.health_potion -= 1
            self.health += 100
            print("Health potion used: You now have {health}hp".format(health = self.health))
            print("You have {} health potion(s) remaining".format(self.health_potion))
        else:
            print("You have run out of health potions!")
            
    def attack(self, enemy):
        if self.strength <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.strength - enemy.defence
            print("{name} attacks {enemy} for {damage} damage!".format(name = self.name, enemy = enemy.name, damage = damage_dealt))
            enemy.lose_health(self.strength)
    
    def cast_spell(self, enemy):
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((enemy.defence * 3)/4)
            print("{name}'s spell hits {enemy} for {damage} damage!".format(name = self.name, enemy = enemy.name, damage = damage_dealt))
            enemy.lose_health(self.spellpower)
    
    def equip_item(self, item):
        self.health += item.health
        self.health_regen += item.health_regen
        self.strength += item.strength
        self.spellpower += item.spellpower
        self.defence += item.defence
        self.health_potion += item.health_potion


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
        if self.health <= 0:
            self.health = 0
            print("{enemy} has been defeated! Well done!".format(enemy = self.name))
        else:
            print("{name} has {health} health remaining".format(name = self.name, health = self.health))

    def attack(self, hero):
        if self.strength <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.strength - hero.defence
            print("{name} attacks {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.strength)
    
    def cast_spell(self, hero):
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((hero.defence * 3)/4)
            print("{name}'s spell hits {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.spellpower)

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
        if self.health <= 0:
            self.health = 0
            print("{boss} has been defeated! Well done!".format(boss = self.name))
        else:
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
    
    def cast_spell(self, hero):
        if self.spellpower <= 0:
            damage_dealt = 0
        else:
            damage_dealt = self.spellpower - ((hero.defence * 3)/4)
            print("{name}'s spell hits {hero} for {damage} damage!".format(name = self.name, hero = hero.name, damage = damage_dealt))
            hero.lose_health(self.spellpower)

# Loot choice of item after defeating each enemy that gives certain stats
class Item:
    
    def __init__(self, name, health = 0, health_regen = 0, strength = 0, spellpower = 0, defence = 0, health_potion = 0):
        self.name = name
        self.health = health
        self.health_regen = health_regen
        self.strength = strength
        self.spellpower = spellpower
        self.defence = defence
        self.health_potion = health_potion
    
    def __repr__(self):
        return self.name, self.health, self.health_regen, self.strength, self.spellpower, self.defence, self.health_potion


# Test Code

# hero = Hero()
# enemy = Enemy("John", 200, 50, 0, 20)

# hero.attack(enemy)
# enemy.attack(hero)
# enemy.attack(hero)
# enemy.attack(hero)
# enemy.attack(hero)
# enemy.attack(hero)

# hero.cast_spell(enemy)
# enemy.cast_spell(hero)

# boss = Boss()
# boss.regen_health()

# viking_shield = Item("Viking Shield", defence = 30)
# hero.use_item(viking_shield)
# print(hero.defence)
# print(hero.__repr__())

# hero.use_health_pot()
# print(hero.health_potion)