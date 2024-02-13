from config import app
import requests
import re

from models import *

if __name__ == "__main__":
  with app.app_context():

    base_url = "https://api.pokemontcg.io/v2/cards"
    test_url = "https://api.pokemontcg.io/v2/sets/sv3pt5"
    params = {
      "t": 'set.id:sv3pt5',               #working
      'r': 'set.releaseDate:2023/09/22',  #not working
      'n': 'name:squirtle'                #working
    }
    limit = "&pageSize=151"
    url = f"{base_url}/?q={params['t']}{limit}"

    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
    else:
      print("Error:", response.status_code)

    pokemon = data["data"]

    counter = 0
    for obj in pokemon:

      if obj["attacks"][0]["damage"] == "" and len(obj["attacks"]) == 1:
        attack = obj["attacks"][0]
      elif obj["attacks"][0]["damage"] == "" and len(obj["attacks"]) >= 2:
        attack = obj["attacks"][1]
      else:
        attack = obj["attacks"][0]
      
      '''Accounts for damage being 0'''

      if attack["damage"] == "":    
        attack["damage"] = 20

      '''Removes all non-int characters'''
      attack["damage"] = str(attack["damage"])
      attack["damage"] = attack["damage"].replace("×", '').replace('+', '')
      attack["damage"] = int(attack["damage"])

      print(f"{counter} -- {attack['damage']} \n {attack['name']} -- {obj['hp']}")
      counter += 1

    #   Pokemon(
    #     name = obj["name"]
    #     starting_hp = obj["hp"]
    #     max_hp = obj["hp"]
    #     attack_name = attack["name"]
    #     attack_damage = attack["damage"]
    #     trainer_id = null
    #   )


 
