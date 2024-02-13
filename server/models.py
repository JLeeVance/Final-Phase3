from config import db

"""Classes"""

# User will be able to Create Trainer or see all Trainers
# View All Trainers
    #list of Trainers
# When a Trainer is selected
    # the user can add pokemon to their team (max 6) from the list
# Battle Pokemon
    #Wild pokemon appears to be fought, one pokemon can fight per battle
    #fake hp variable used to print the decrementing Hp, but not actually affect the starting HP
    # If lose (trainer_pokemon Hp is 0, force exit to main screen, choose new trainer), all pokemon removed? Or dead pokemon removed?
    # If win (wild_opponent HP is 0, exit back to trainer home page to see all pokemon, and view all trainers.)


class Trainer(db.Model):

    __tablename__ = "trainers"

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.Integer)
    motto = db.Column(db.String)

    # pokemons = db.relationship("Pokemon", back_populates = "trainer")


class Pokemon(db.Model):

    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String)
    starting_hp = db.Column(db.Integer)
    max_hp = db.Column(db.Integer)
    attack_name = db.Column(db.String)
    attack_damage = db.Column(db.Integer)

    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.id"), nullable=True)

    # trainer = db.relationship("Trainer", back_populates = "pokemons")
    # battles = db.relationship("Battle", back_populates = "pokemons" )


class Battle(db.Model):

    __tablename__ = "battles"

    id = db.Column(db.Integer, primary_key = True)

    trainer_pokemon = db.Column(db.Integer , db.ForeignKey('pokemons.id'))
    wild_pokemon = db.Column(db.Integer , db.ForeignKey('pokemons.id'))

    # pokemons = db.relationship("Pokemon", back_populates = "battles")

    
