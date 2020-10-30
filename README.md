# PokeTourney

### Simulador de torneo pokemón!


pokeTourney es un simulador de torneo en el que participan 8 pokemones elegidos al azar dentro de los
primero 155 pokemones en la base de datos de la API [PokeAPI](https://pokeapi.co/).

Podras ver en consola como pelean automáticamente los distintos pokemones para saber quien será el campeón!

---
## Como Usar
Puedes descargar el codigo como un zip o clonar este repositorio. Cuando ya tengas lo necesario debes asegurarte que tienes las librerias para poder correr el juego. Para esto usa la siguiente instrucción en la línea de comandos:

`pip install -r requirements.txt`

Luego simplemente corre el archivo *main.py* con python3 o el ambiente de python en el que hayas instalado los requerimientos. 

A continuación podrá ver las batallas pokemón!

---

## ¿Cómo se decide quién gana?
Para decidir qué pokemón agana cada batalla se calcula su ataque y defensa en base a sus atributos básicos. Se suman los atributos ofensivos (*ataque y ataque especial*) para obtener el ataque y los atributos defensivos (*vida, defensa y defensa especial*) para obtener la defensa.

Luego según los tipos de los pokemones se asigna un modificador que se aplica sobre el ataque.

Así se calcula el daño hecho por un pokemón como:

***daño = modificador * ataque - otroPokemon.defensa***

Gana el pokemón que inflija mayor daño al adversario. Si hay un empate, gana el que tenga mayor velocidad. 
