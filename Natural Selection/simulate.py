import environment as e
import time

def create_environment(color, preys, preys_specie, predators, predators_specie):
    env = e.environment(color, preys, preys_specie, predators, predators_specie)
    return env

def cycle_minutes(env,minutes):
    start =  abs(time.localtime().tm_hour*60 + time.localtime().tm_min)
    now = abs(time.localtime().tm_hour*60 + time.localtime().tm_min)

    env.reproduce()
    env.hunt()
    env.reproduce()
    env.die()
    env.count_animals()
    env.count_colors()

    while now - start < minutes:

        last_minute = now
        now = abs(time.localtime().tm_hour*60 + time.localtime().tm_min)

        if last_minute != now:
            env.reproduce()
            env.hunt()
            env.reproduce()
            env.die()
            env.count_animals()
            env.count_colors()

env = create_environment("green",20,"frog",12,"snake")
cycle_minutes(env,20)