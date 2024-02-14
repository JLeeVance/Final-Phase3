from models import *
import random
# from flask import Flask

def get_all_pokemon():
    return db.session.query(Pokemon).all()

def get_pokemon_by_id(poke_id):
    return db.session.query(Pokemon).get(poke_id)

def show_pokemon_trainer_name(trainer_id):
    trainer = get_trainer_by_id(trainer_id)
    return trainer.name

def show_pokemon_name(pokemon_id):
    poke = get_pokemon_by_id(pokemon_id)
    return poke.name

def get_all_trainers():
    return db.session.query(Trainer).all()

def get_trainer_by_id(trainer_id):
    return db.session.query(Trainer).get(trainer_id)

def get_trainer_count():
    return db.session.query(Trainer).count()

def add_trainer_to_table(
        name,
        age,
        motto
):
    new_trainer = Trainer(
        name=name,
        age=age,
        motto=motto
    )
    db.session.add(new_trainer)
    db.session.commit()

def get_trainers_pokemon(trainers_id):
    return db.session.query(Pokemon).filter_by(trainer_id = f"{trainers_id}").all()

def handle_pokemon_release(poke_id):
    poke = get_pokemon_by_id(poke_id)
    poke.trainer_id = None
    db.session.commit()

def get_available_pokemon():
    return db.session.query(Pokemon).filter_by(trainer_id=None).all()

def handle_pokemon_add(choice, new_trainer_id):
    poke = get_pokemon_by_id(choice)
    poke.trainer_id = new_trainer_id
    db.session.commit()

def get_random_wild():
    wild_pokemon_list = get_available_pokemon()
    wild_pokemon = random.choice(wild_pokemon_list)
    return wild_pokemon

def reduce_wild_hp(wild_pokemon, attack_damage):
    wild_pokemon.starting_hp -= attack_damage
    db.session.commit()

def reduce_trainer_pokemon(pokemon, wild_attack_damage):
    pokemon.starting_hp -= wild_attack_damage
    db.session.commit()

def handle_add_battle(pokemon, wild_pokemon):
    battle = Battle(trainer_pokemon = pokemon.id, wild_pokemon = wild_pokemon.id)
    db.session.add(battle)
    db.session.commit()

def handle_reset_pokemon(pokemon):
    pokemon.starting_hp = pokemon.max_hp
    db.session.commit()

def handle_delete_trainer(choice):
    trainer = get_trainer_by_id(choice)
    db.session.delete(trainer)
    db.session.commit()