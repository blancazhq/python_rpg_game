"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
import sys

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        #time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):


    def __init__(self):
        items = [Tonic(), Sword(), Supertonic(), Armer(), Evade(), Darktonic(), Swap()]

        self.name = 'hero'
        self.health = 15
        self.power = 5
        self.coins = 20
        self.armorpoints = 0
        self.evadepoints = 5
        self.darkpoints = 0
        self.stuff = {items[0].__hash__():[], items[1].__hash__():[], items[2].__hash__():[], items[3].__hash__():[], items[4].__hash__():[], items[5].__hash__():[], items[6].__hash__():[]}


    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        a = random.randint(1, 10)
        if a > 2:
            enemy.receive_damage(self.power)
        else:
            enemy.receive_damage(self.power*2)
        #time.sleep(0.5)

    def receive_damage(self, points):
        x = 0.05 + self.evadepoints / 2 * 0.05
        a = random.randint(1, 10)
        if a > 10 * x:
            self.health -= (points-self.armorpoints)
        else:
            pass
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        #time.sleep(0.5)

    def buy(self, item):
        self.coins -= item.cost
        self.stuff[item.__hash__()].append(item)
        print "you have purchased %s." % item.name
        sys.stdout.write ("you stuff list: ")
        for key, value in self.stuff.items():
            if value != []:
                sys.stdout.write((value[0].name)+ " x " + str(len(value)) + " ")
        print "\n"

    def carry(self, item):
        item.apply(hero,enemy)
        self.stuff[item.__hash__()].remove(self.stuff[item.__hash__()][0])

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Zombie(Character):

    def __init__(self):
        self.name = "zombie"
        self.health = 1
        self.power = 2
        self.bounty = 3
        self.survive = True

    def alive (self):
        if self.survive == True:
            return True

    def print_status (self):
        print "Zombie's status is a secret. But I can tell you it never dies"

    def receive_damage(self, points):
        a = random.randint(1, 10)
        if a > 1:
            pass
        else:
            self.health -= points
        print "%s received %d damage." % (self.name, points)


class Medic(Character):

    def __init__(self):
        self.name = "medic"
        self.health = 5
        self.power = 2
        self.bounty = 5

    def receive_damage(self, points):
        a = random.randint(1, 10)
        if a > 2:
            self.health -= points
        else:
            self.health -= points
            self.health +=2
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Shadow(Character):

    def __init__(self):
        self.name = "shadow"
        self.health = 1
        self.power = 2
        self.bounty = 5

    def receive_damage(self, points):
        a = random.randint(1, 10)
        if a > 1:
            pass
        else:
            self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Bountymax (Character):

    def __init__(self):
        self.name = "bountymax"
        self.health = 15
        self.power = 2
        self.bounty = 30

class Randomit (Character):

    def __init__(self):
        self.name = "randomit"
        self.health = 5
        self.power = 3
        self.bounty = 5

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        a = random.randint(1, 10)
        enemy.receive_damage(random.randint(1, 10))
        #time.sleep(1.5)


class Battle(object):

    def do_battle(self, hero, enemy):
        items = [Tonic(), Sword(), Supertonic(), Armer(), Evade(), Darktonic(), Swap()]


        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            ##time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                if hero.stuff == {items[0].__hash__():[], items[1].__hash__():[], items[2].__hash__():[], items[3].__hash__():[], items[4].__hash__():[], items[5].__hash__():[], items[6].__hash__():[]}:
                    print "No stuff to carry for now."
                else:
                    print "-----------------------"
                    print "What do you want to carry? ("
                    my_list = []
                    for key, value in hero.stuff.items():
                        if value != []:
                            my_list.append(value[0].name)
                    for i in range(len(my_list)):
                        print str(i+1) + ". " + str(my_list[i])
                    print str(len(my_list)+1) + ". nothing"
                    print "> ",
                    input = int(raw_input())
                    if input in range(len(my_list)+1):
                        for i in range(0, len(items)):
                            if items[i].name == my_list[input-1]:
                                hero.carry(item[i])
                                break
                    if input == len(my_list)+1:
                            print "Carry nothing"
                hero.attack(enemy)
                if hero.darkpoints >=5:
                    enemy.survive = False
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue

            enemy.attack(hero)
        if hero.alive() and enemy.name != "zombie":
            print "You defeated the %s" % enemy.name
            hero.coins += enemy.bounty
            print "You receive %d coins" % enemy.bounty
            return True
        elif hero.alive() and enemy.name == "zombie":
            if enemy.survive == False:
                print "%s is dead." % enemy.name
                print "You defeated the %s" % enemy.name
                hero.coins += enemy.bounty
                print "You receive %d coins" % enemy.bounty
                return True
        else:
            print "YOU LOSE!"
            return False

class Stuff(object):

    def __hash__(self):
        return hash(self.name)


class Tonic(Stuff):
    cost = 5
    name = 'tonic'
    def apply(self, hero, enemy):
        hero.health += 2
        print "%s applied." % self.name
        print "%s's health increased to %d." % (hero.name, hero.health)

class Supertonic(Stuff):
    cost = 30
    name = 'supertonic'
    def apply(self, hero, enemy):
        hero.health += 10
        print "%s applied." % self.name
        print "%s's health increased to %d." % (hero.name, hero.health)

class Sword(Stuff):
    cost = 10
    name = 'sword'
    def apply(self, hero, enemy):
        hero.power += 2
        print "%s applied." % self.name
        print "%s's power increased to %d." % (hero.name, hero.power)

class Armer(Stuff):
    cost = 20
    name = 'armer'
    def apply(self, hero, enemy):
        hero.armorpoints += 2
        print "%s applied." % self.name
        print "%s's armorpoints increased to %d." % (hero.name, hero.armorpoints)

class Evade(Stuff):
    cost = 10
    name = 'evade'
    def apply(self, hero, enemy):
        if hero.evadepoints < 38:
            hero.evadepoints += 2
            print "%s applied." % self.name
            print "%s's evadepoints increased to %d." % (hero.name, hero.evadepoints)
            print "%s's possibility to avoid attach is %s" % (hero.name, str(100 * (0.05 + hero.evadepoints / 2 * 0.05)) + "%")
        if hero.evadepoints < 38:
            print "%s cannot be applied. Because your evadepoints has reached maximum." % self.name
            pass

class Darktonic(Stuff):
    cost = 20
    name = 'darktonic'
    def apply(self, hero, enemy):
        hero.health -= 5
        hero.darkpoints += 5
        print "%s's health decreased to %d." % (hero.name, hero.health)
        print "%s's darkpoints decreased to %d." % (hero.name, hero.darkpoints)

class Swap(Stuff):
    cost = 10
    name = 'swap'
    def apply(self, hero, enemy):
        print "%s swaps power with %s during attack" % (hero.name, enemy.name)
        hero.power, enemy.power = enemy.power, hero.power

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Supertonic, Armer, Evade, Darktonic, Swap]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            if hero.coins <= 0:
                print "Out of money. Defeat someone to get more"
                break
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)



hero = Hero()
enemies = [Goblin(), Wizard(), Medic(), Shadow(), Bountymax(), Randomit(), Zombie()]
item = [Tonic(), Sword(), Supertonic(), Armer(), Evade(), Darktonic(), Swap()]
battle_engine = Battle()
shopping_engine = Store()



for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "GAME OVER!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
