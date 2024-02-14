from models import *
# from flask import Flask

def get_all_pokemon():
    return db.session.query(Pokemon).all()

def get_pokemon_by_id(poke_id):
    return db.session.query(Pokemon).get(poke_id)

def show_pokemon_trainer(trainer_id):
    trainer = db.session.query(Trainer).get(trainer_id)
    name = trainer.name
    return name

def get_all_trainers():
    return db.session.query(Trainer).all()
