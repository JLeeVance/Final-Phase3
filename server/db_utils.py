from models import *
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