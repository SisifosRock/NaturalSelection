import animal as a
import random, time

colors = ["green", "grey", "blue", "yellow", "red", "pink", "purple"]

def roll_dice(possib):
    return random.choice(range(possib))

class environment:

    def __init__(self, fav_color, preys_number, preys_specie, predators_number, predators_specie):

        assert fav_color in colors, "this is not a valid argument (color)"

        self.preys = [a.prey(preys_specie,fav_color,0)]
        self.predators = [a.predator(predators_specie,0)]
        self.fav_color = fav_color

        for i in range(preys_number):
            p = a.prey(preys_specie, random.choice(colors), 0)
            self.preys.append(p)

        for i in range(predators_number):
            p = a.predator(predators_specie, 0)
            self.predators.append(p)

    def reproduce(self):
        for i in self.preys:
            j = random.choice(self.preys)

            if (i != j and i.specie == j.specie) and (roll_dice(20) > 7 and i.generation == j.generation):

                possible_colors = [i.color, j.color]

                son = a.prey(i.specie, random.choice(possible_colors), i.generation + 1)
                self.preys.append(son)

        for i in self.predators:
            j = random.choice(self.predators)

            if (i != j and i.specie == j.specie) and (roll_dice(20) > 10 and i.generation == j.generation):

                son = a.predator(i.specie, i.generation + 1)
                self.predators.append(son)

    def hunt(self):
        for i in self.predators:
            try:
                p = random.choice(range(len(self.preys)))
                if self.preys[p].color == self.fav_color and roll_dice(20) > 16:
                    i.hungry = 0
                    del self.preys[p]

                elif self.preys[p].color != self.fav_color and roll_dice(20) > 10:
                    i.hungry = 0
                    del self.preys[p]

            except IndexError:
                print("All the preys are dead")
                break
    
    def die(self):
        for i in range(len(self.preys) - 1):
            self.preys[i].ages()
            if self.preys[i].age >= self.preys[i].max_age:
                del self.preys[i]

        for i in range(len(self.predators) - 1):
            self.predators[i].ages()
            if self.predators[i].age >= self.predators[i].max_age:
                del self.predators[i]

            if self.predators[i].hungry > 1:
                del self.predators[i]

    def count_animals(self):
        c_a = {"Preys" : len(self.preys), "Predators" : len(self.predators)}

        print(c_a)
        #print("{} preys and {} predators".format(len(self.preys), len(self.predators)))

    def count_colors(self):
        p_c = {}

        for col in colors:
            p_c[col] = 0

        for obj in self.preys:
            p_c[obj.color] += 1

        print(p_c)