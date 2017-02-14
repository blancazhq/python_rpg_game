"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def alive (self):
        if self.health > 0:
            return True

    def print_status (self):
        print "%s have %d health and %d power." % (self.name, self.health, self.power)

    def attack (self, someone):
        someone.health -= self.power
        print "The %s do %d damage to %s." % (self.name, self.power, someone.name)
        if someone.health <= 0:
            print "the %s is dead." % someone.name


class Hero(Character):


    def __init__(self, name, hero_health, hero_power):
        self.name = name
        self.health = hero_health
        self.power = hero_power



class Goblin(Character):


    def __init__(self, name, goblin_health, goblin_power):
        self.name = name
        self.health = goblin_health
        self.power = goblin_power



class Zombie(Character):


    def __init__(self, name, zombie_health, zombie_power):
        self.name = name
        self.health = zombie_health
        self.power = zombie_power



def main():
    hero = Hero("hero", 5, 3)
    goblin = Goblin("goblin", 6, 2)
    zombie = Zombie("zombie", 1, 3)

    while hero.alive() and goblin.alive():
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.health > 0:
            zombie.attack(hero)
            goblin.attack(hero)




main()
