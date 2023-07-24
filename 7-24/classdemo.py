# PLAYER CHARACTER OBJECT

 # best practice states to ALWAYS capitalize your class names!
 # makes it easier to tell that an object is a class
class Hero:
    def __init__(self, hitpoints, dexterity, strength):    # constructor
             self.str=  strength
             self.dex=  dexterity
             self.int=  10
             self.HP=   hitpoints

     # when activated, the potion will increase HP by a certain number
    def potion(self, amount):
        # self.hp to increase by the amount specified
        self.HP += amount

    def punch(self, target):
        # target's HP to decrease by a number contingent on the player's strength
        damage = self.str/3
        target.HP -= damage

# maria is a ROGUE hero
maria= Hero(9, 18, 9)

# sal is a WARRIOR hero
sal= Hero(12, 10, 18)

# CLASS ATTRIBUTES

print("Sal's hitpoints are", sal.HP)

print("Maria punches Sal in the face!")
maria.punch(sal)

print("Sal's hitpoints are", sal.HP)

print("Sal drinks a potion!")
sal.potion(5)

print("Sal's hitpoints are", sal.HP)

maria.punch("Chad")


