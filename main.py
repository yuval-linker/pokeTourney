"""
 @author: Yuval Linker
 Pokemon Tourney code
 Para postular a Internship en Platanus
"""

import tourney as tn
import random

if __name__ == '__main__':
    # Se obtienen 8 ids de pokemones al azar e inicializa una lista con los pokemones
    pk_ids = random.sample(range(1, 156), k=8)
    pokemons = [tn.pb.pokemon(num) for num in pk_ids]

    print("Los pokemones elegidos son:")
    for pkmn in pokemons:
        print("\t" + pkmn.name.title())
    print()
    print("Comienza el torneo!\n", flush=True)

    # Se hace el torneo
    tn.tourney(pokemons)