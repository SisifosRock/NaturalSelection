import environment as e
import time

def create_environment(color, preys, preys_specie, predators, predators_specie):
    env = e.environment(color, preys, preys_specie, predators, predators_specie)
    return env

def cycle_minutes(env,minutes):
    start =  abs(time.localtime().tm_min*60 + time.localtime().tm_sec)
    now = abs(time.localtime().tm_min*60 + time.localtime().tm_sec)

    env.count_animals()
    env.count_colors()
    print("\n ")
    env.reproduce()
    env.hunt()
    env.reproduce()
    env.reproduce()
    env.die()
    env.count_animals()
    env.count_colors()
    print("\n ")

    while now - start < minutes*60 and len(env.preys) > 0:

        last_sec = now
        now = abs(time.localtime().tm_min*60 + time.localtime().tm_sec)

        if last_sec != now:
            env.reproduce()
            env.hunt()
            env.reproduce()
            env.reproduce()
            env.die()
            env.count_animals()
            env.count_colors()
            print("\n ")

env = create_environment("green",200,"frog",100,"snake")
cycle_minutes(env,1)

