# Two fighters, one winner.
# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.health < fighter2.damage_per_attack and fighter2.health < fighter1.damage_per_attack:
        return first_attacker
    elif fighter1.health / fighter2.damage_per_attack > fighter2.health / fighter1.damage_per_attack:
        return fighter1.name
    elif fighter1.health / fighter2.damage_per_attack < fighter2.health / fighter1.damage_per_attack:
        return fighter2.name
    else:
        return first_attacker
