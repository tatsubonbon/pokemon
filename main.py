import random

from application.pokemonGenerator import PokemonGenerator
from model.garura import Garura
from model.pikachu import Pikachu

try:
    # generator = PokemonGenerator()
    pikachu = Pikachu()
    # opponent = generator.getOpponent()
    opponent = Garura()
    while True:
        for i, tequnique in enumerate(pikachu.tequniques):
            print(str(i) + ":" + tequnique.name)
        tequniqueIndex = input("技を選択してください。")
        print("#########################")
        # if pikachu.speed.speed > opponent.speed.speed:
        #     pikachu.attack(int(tequniqueIndex), opponent)
        pikachu.attack(int(tequniqueIndex), opponent)
        print("#########################")
        opponent.attack(0, pikachu)
        print("#########################")
except ValueError as e:
    print(e)
