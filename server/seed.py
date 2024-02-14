from config import app
import requests
import random

from models import *

if __name__ == "__main__":
  with app.app_context():

    Pokemon.query.delete()
    Trainer.query.delete()
    db.session.commit()

    base_url = "https://api.pokemontcg.io/v2/cards"
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

    for obj in pokemon:

      '''Attempts to select one attack with a present value for 'damage'''

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

      poke = Pokemon(
        name = obj["name"],
        starting_hp = obj["hp"],
        max_hp = obj["hp"],
        attack_name = attack["name"],
        attack_damage = attack["damage"]
      )
      db.session.add(poke)
      db.session.commit()

    trainer_mottos = [
    "Catch 'em all, Train 'em best!",
    "Battles won with skill, bonds built with heart.",
    "Victory through strategy, friendship, and determination.",
    "Every challenge is a step towards mastery.",
    "From Pikachu to Legendary, I'll conquer them all.",
    "Training Pokémon, forging champions.",
    "With courage and Pokémon, anything is possible.",
    "In the pursuit of excellence, every Pokémon matters.",
    "Through teamwork and training, we rise to the top.",
    "Trainer by passion, champion by choice."
    ]
    trainer_names = [
    "Ash Ketchum",
    "Misty Waterflower",
    "Brock Pewter",
    "Serena",
    "Gary Oak",
    "May Maple",
    "Dawn Berlitz",
    "Cynthia Shirona",
    "Wendy, Williamson",
    "George"
    ]

    for x in range(10):
      train = Trainer(
        name = random.choice(trainer_names),
        motto = random.choice(trainer_mottos),
        age = random.choice(range(10,50))
        )
      db.session.add(train)
      db.session.commit()
 
