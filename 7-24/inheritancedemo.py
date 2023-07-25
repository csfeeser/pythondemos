# PLAYER CHARACTER OBJECT
class Hero:
    def __init__(self, hitpoints, dexterity, strength):   
             self.str=  strength
             self.dex=  dexterity
             self.HP=   hitpoints

    def potion(self, amount):
        self.HP += amount

    def punch(self, target):
        damage = self.str/3
        target.HP -= damage

# CLASS INHERITANCE - taking a generic class and building on top of it, adding/changing attributes and methods!

class Mage(Hero):
    def __init__(self, hitpoints, dexterity, strength, intelligence):
        self.int = intelligence

    def fireball(self, target):
        target.HP -= self.int * 2

class Warrior(Hero):
    def sword(self, target):
        target.HP -= self.str + 2

james = Mage(8, 12, 8, 18)    # mage
nor   = Warrior(hitpoints=10, dexterity=10, strength=18)    # warrior

print("Pre-fireball, Nor's HP is:", nor.HP)
james.fireball(nor)
print("Post-fireball, Nor's HP is:", nor.HP)

print("Nor shakes it off and drinks a potion!")
nor.potion(30)
print("Post-potion, Nor's HP is:", nor.HP)

