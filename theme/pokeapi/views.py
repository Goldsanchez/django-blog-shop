from django.shortcuts import render
import requests # Aunque lo marca, FUNCIONA
import random
# Create your views here.



def pokeApi(request):

    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num1}/')
    pokemonJsonOne = response.json()
    
    responseTwo = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num2}/')
    pokemonJsonTwo = responseTwo.json()

    return render(request, "pokeapi/pokemones.html", {"pokemonOne": pokemonJsonOne, "pokemonTwo":pokemonJsonTwo})

