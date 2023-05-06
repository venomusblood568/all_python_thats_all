
import os

for i in range(1,899):
    os.system("curl https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{:03d}.png -o ./pokemon_final_test/{}.png".format(i ,i))
print("task done")
