import animal as a
import random, time

colors = ["green", "grey", "blue", "yellow", "red", "pink", "purple"]

def roll_dice(possib):
    return random.choice(range(possib))

class environment:

    def __init__(self, fav_color, preys_number, preys_specie, predators_number, predators_specie):

        assert fav_color in colors, "this is not a valid argument (color)"

        self.preys = [a.prey(preys_specie,fav_color,0, random.randint(3,8))]
        self.predators = [a.predator(predators_specie,0, random.randint(3,8))]
        self.fav_color = fav_color

        for prey_index in range(preys_number):
            p = a.prey(preys_specie, random.choice(colors), 0, random.randint(7,14))
            self.preys.append(p)

        for pred_index in range(predators_number):
            p = a.predator(predators_specie, 0, random.randint(7,15))
            self.predators.append(p)

    def reproduce(self):
        for prey1 in self.preys:
            prey2 = random.choice(self.preys)
            while prey1 == prey2 and len(self.preys) > 1:
                prey2 = random.choice(self.preys)

            if len(self.preys) <= 1:
                break

            if (prey1.specie == prey2.specie) and (roll_dice(20) > 7 and prey1.generation == prey2.generation):

                possible_colors = [prey1.color, prey2.color]
                possible_ages = [prey1.max_age, prey2.max_age]

                son = a.prey(prey1.specie, random.choice(possible_colors), prey1.generation + 1, random.choice(possible_ages))
                self.preys.append(son)

        for pred1 in self.predators:
            pred2 = random.choice(self.predators)
            while pred1 == pred2 and len(self.predators) > 1:
                pred2 = random.choice(self.predators)

            if len(self.predators) <= 1:
                break

            possible_ages = [pred1.max_age, pred2.max_age]

            if (pred1 != pred2 and pred1.specie == pred2.specie) and (roll_dice(20) > 9 and pred1.generation == pred2.generation):

                son = a.predator(pred1.specie, pred1.generation + 1, random.choice(possible_ages))
                self.predators.append(son)

    def hunt(self):
        
        try:
            dead_preys = []
            for i in self.predators:

                p = random.choice(range(len(self.preys)))
                while p in dead_preys and len(dead_preys) != len(self.preys):
                    p = random.choice(range(len(self.preys)))
                    if len(dead_preys) >= len(self.preys):
                        raise IndexError

                if p in dead_preys:
                    raise IndexError

                if self.preys[p].color == self.fav_color and roll_dice(20) > 16:

                    i.hungry = 0
                    dead_preys.append(p)

                elif self.preys[p].color != self.fav_color and roll_dice(20) > 12:

                    i.hungry = 0
                    dead_preys.append(p)

            if len(dead_preys) > 0:
                print("Preys hunted: {}".format(len(dead_preys)))
                dead_preys.sort()

                for dead in dead_preys[::-1]:
                    del self.preys[dead]

        except IndexError:
            self.preys = []
            print ("All preys are dead")
            return 0



    def die(self):
        dead_preys = []
        dead_preds = []
        hungry_death_count = 0

        for i in range(len(self.preys)):
            self.preys[i].ages()
            if self.preys[i].age >= self.preys[i].max_age:
                dead_preys.append(i)

        for i in range(len(self.predators)):
            self.predators[i].ages()
            if self.predators[i].age >= self.predators[i].max_age:
                dead_preds.append(i)

            elif self.predators[i].hungry > 1:
                hungry_death_count += 1
                dead_preds.append(i)
        
        print("Preys that died from age: ", len(dead_preys))
        print("Preds that died from starving: ", hungry_death_count)

        for dead in dead_preys[::-1]:
            
            del self.preys[dead]

        for dead in dead_preds[::-1]:

            del self.predators[dead]

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