import random, time

colors = ["green", "grey", "blue", "yellow", "red", "pink", "purple"]


class prey:
    def __init__(self, specie, color, generation, max_age):

        assert color in colors, "this is not a valid argument (color)"

        self.birthday = [time.localtime().tm_min, time.localtime().tm_sec]
        self.specie = specie
        self.color = color
        self.generation = generation
        self.age = 0
        self.max_age = max_age

    def ages(self):
        self.age = abs((time.localtime().tm_min*60 + time.localtime().tm_sec) - (self.birthday[0]*60 + self.birthday[1]))

class predator:
    def __init__(self, specie, generation, max_age):
        self.birthday = [time.localtime().tm_min, time.localtime().tm_sec]
        self.specie = specie
        self.generation = generation
        self.age = 0
        self.max_age = max_age
        self.hungry = 0

    def ages(self):
        last_age = self.age
        self.age = abs((time.localtime().tm_min*60 + time.localtime().tm_sec) - (self.birthday[0]*60 + self.birthday[1]))

        if last_age != self.age:
            self.hungry += self.age - last_age
