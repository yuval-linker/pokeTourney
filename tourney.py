"""
    @author: Yuval Linker
    Modulo tourney con funciones para simular un torneo pokemon
"""

import pokebase as pb


# STATS: 0: hp, 1: attack, 2: defense, 3: sp.attack, 4: sp.defense, 5: speed
"""
Asigna los atributos de ataque y defensa de un pokemón.
Esto se hace asignando todos los atributos ofensivos al ataque y todos los defensivos a la defensa
"""
def pkmn_stats(stats):
    atk = stats[1].base_stat + stats[3].base_stat
    defense = stats[0].base_stat + stats[3].base_stat + stats[4].base_stat
    return (atk, defense)


"""
Retorna los modificadores de los pokemones dependiendo del tipo de cada uno
    @params types
        Lista de tipos del pokemon 1
    @params other_types
        Lista de tipos del pokemon 2
    @return
        Una tupla con ambos modificadores (int, int)
"""
# Como estan las relaciones hacia ambos lados solo necesito revisar una vez.
def pkmn_modifier(types, other_types):
    mymod = 1
    othermod = 1
    
    ddfrom = set()
    ddto = set()
    hdfrom = set()
    hdto = set()
    ndfrom = set()
    ndto = set()

    def name_getter(elem):
        return elem.name

    for type_slot in other_types:
        t = pb.type_(type_slot.type.name).damage_relations
        ddfrom.update(map(name_getter, t.double_damage_from))
        ddto.update(map(name_getter, t.double_damage_to))
        hdfrom.update(map(name_getter, t.half_damage_from))
        hdto.update(map(name_getter, t.half_damage_to))
        ndfrom.update(map(name_getter, t.no_damage_from))
        ndto.update(map(name_getter, t.no_damage_to))
    
    for type_slot in types:
        name = type_slot.type.name
        # print(name)
        if name in ndfrom:
            mymod = 0
        if name in ndto:
            othermod = 0
        if name in hdto:
            othermod = 0.5
        if name in hdfrom:
            mymod = 0.5
        if name in ddto:
            othermod = 2
        if name in ddfrom:
            mymod = 2

    return (mymod, othermod) 



"""
Simula una batalla entre dos pokemones
para esto se basa en los base_stats y los tipos
    @params pk1, pk2
        Los pokemones. Su tipo es APIresource de la libreria pokebase

    @returns
        True si gana pk1, falso si gana pk2 
"""
def fight(pk1, pk2):
    name1 = pk1.name.title()
    name2 = pk2.name.title()
    print(f"Los pokemones {name1} y {name2} estan batallando!\n", flush=True)
    stats1 = pk1.stats
    stats2 = pk2.stats
    # Vamos a tomar los stats de defensa. Por simplicidad no van a modificarse
    # Las modificaciones seran sobre los stats de ataque.
    (atk1, defense1) = pkmn_stats(stats1)
    print(f"{name1} tiene un ataque de {atk1} y una defensa de {defense1}")
    (atk2, defense2) = pkmn_stats(stats2)
    print(f"{name2} tiene un ataque de {atk2} y una defensa de {defense2}")

    # Buscamos los modificadores por el tipo
    (mod1, mod2) = pkmn_modifier(pk1.types, pk2.types)

    print(f"Los modificadores son {mod1} para {name1} y {mod2} para {name2}")
    atk1 *= mod1
    atk2 *= mod2

    dmg1 = atk1 - defense2
    dmg2 = atk2 - defense1

    print(f"El pokemón {name1} ha inflingido {dmg1} puntos de daño")
    print(f"El pokemón {name2} ha inflingido {dmg2} puntos de daño", flush=True)
    
    # CASO EMPATE: se define por velocidad
    if dmg1 == dmg2:
        winner = pk1 if stats1[5].base_stat > stats2[5].base_stat else pk2
    else:
        winner =  pk1 if dmg1 > dmg2 else pk2

    print(f"El ganador de esta batalla es {winner.name.title()}!\n", flush=True)
    return winner

"""
Simula todas las batallas de una fase del torneo.

    @params pkmns
        Lista de pokemones que batallan en esta fase
    @return
        Lista con los pokemones ganadores
"""
def bracket(pkmns):
    if len(pkmns) == 2:
        print("Comienza la final!\n")
    else:
        print(f"Comienza la fase {8 // len(pkmns)}:\n")
    winners = []
    for i in range(len(pkmns) // 2):
        print(f"\t {pkmns[2*i].name.upper()} V/S {pkmns[2*i + 1].name.upper()}\n")
        winners.append(fight(pkmns[2*i], pkmns[2*i + 1]))
    return winners


"""
Simula el torneo
"""
def tourney(pkmns):
    # TODO: Implementar el torneo
    while(len(pkmns) > 1):
        pkmns = bracket(pkmns)
    
    print(f"El ganador del torneo es el pokemón {pkmns[0].name.title()}!!\nFelicidades!")