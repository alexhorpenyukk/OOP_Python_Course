#################
## CHALLENGE 2 ##
#################

# Requirements
# * Define a Password class that supports two instance attributes: strength and length
# * The class should generate a random password having the following characteristics, depending on strength:
# - low: include a mix of 8 lowercase and uppercase letters only
# - mid: a mix of 12 lowercase and uppercase letters and numbers
# - high: a mix of 16 lowercase and uppercase letters and numbers and punctuation signs
# * If the user specifies a length, the user-specified one overrides the defaults above
# * If the user does not specify a strength, assume "high"
# * Finally, the class should also implement a method called show_input_universe() which is not specific to the instance.
# The method should return a dict of lists exposing the pools of characters from where the sampling is done, e.g.
# {"letters": ["a", "b"...], "numbers": [0, 1, 2...], "punctuation": ["!", "?"...]}.

# Example Usage
# p1 = Password(strength="low")
# p1.password
# LAyuu4EI

# p2 = Password(strength="mid", length=37)
# p2.password
# D6tjKt885vM2U5IwHYqhr9aL6SbIBhHJ16gZf

# p3 = Password(strength="high")
# p3.password
# 71'Z>fG{9gIUQQ2a

# p4 = Password()
# p4.password
# IGYY2veeqz1Q

from string import ascii_letters, punctuation, digits
import random


class Password:

    INPUT_UNIVERSE = {
        "letters": list(ascii_letters),
        "numbers": list(digits),
        "punctuation": list(punctuation),
    }

    LENGTHS = {"low": 8, "mid": 12, "high": 16}

    def __init__(self, strength="mid", length=None):
        self.strength = strength
        self.length = length or self.LENGTHS[strength]

    def generate_password(self):

        population = self.INPUT_UNIVERSE["letters"]

        if self.strength == "mid":
            population += self.INPUT_UNIVERSE["numbers"]

        elif self.strength == "high":
            population += (
                self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
            )

        password = "".join(list(map(str, random.choices(population, k=self.length))))
        return password
    
    def show_input_universe(self):
        return self.INPUT_UNIVERSE            
