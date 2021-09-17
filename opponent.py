##
# opponent.py
# Date: 09/09/2021
# Author: Ryan Gordon
# Contains the opponent class for the dental RPG

import random
from math import ceil
from time import sleep
from print_options import print_slow
from constants import STAGES, OPPONENTS, SPECIFIC_MOB_ATTACKS


class Opponent:
    """Creates an opponent object."""

    def __init__(self, stage):
        """
        Basic setup and variables for the computer opponent.

        param stage (int): battle the player is up to, determines available
        opponents when choosing an opponent and slightly increases opponent
        health with each stage.
        """

        # Determine opponent randomly based off the stage
        available_levels, available_opponents = STAGES[stage], []
        for opponent in OPPONENTS:
            if OPPONENTS[opponent][1] in available_levels:
                available_opponents.append(opponent)
        self.name = random.choice(available_opponents)

        # Determine health with a random component
        base_health = OPPONENTS[self.name][0]
        self.health = random.randint(base_health - 5, base_health + 5)
        # The more battles the user fights, the higher the health, also random
        self.health += ceil(random.randint(stage - 1, stage + 2) * 1.5)

        # Determine available attacks based off the chosen opponent
        self.attacks = []
        for attack in SPECIFIC_MOB_ATTACKS:
            if self.name in SPECIFIC_MOB_ATTACKS[attack]:
                self.attacks.append(attack)

        # Print encounter message
        print_slow("You have encountered: ", '')
        sleep(1)
        print_slow(self.name + "!")

    def add_attack(self, attack):
        """Adds a new attack to an opponent."""
        self.attacks.append(attack)

    def get_attack(self):
        """Chooses a random attack and returns it."""
        return random.choice(self.attacks)

    def get_status(self):
        """Returns True if alive, False is dead."""
        return self.health > 0

    def take_damage(self, damage):
        """Reduces health based on user damage."""
        self.health -= damage