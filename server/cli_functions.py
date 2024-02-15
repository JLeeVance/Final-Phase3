from models import *
import os
import time

from rich import *
from rich import print
from rich.console import Console
from rich.align import Align
from rich.padding import Padding
from rich.text import Text

from db_utils import *
'''db.session'''


''' Global Use-Functions '''

console = Console()

def six_second_timer():
   time.sleep(6)

def three_second_timer():
   time.sleep(3)

def two_second_timer():
   time.sleep(2)

def one_second_timer():
   time.sleep(1)

def clear():
  os.system('clear')

def two_line_space():
   print("\n" * 2)

def four_line_space():
   print("\n" * 4)

def print_error():
   clear()
   console.print(Align.center(Padding(" !! Your selection must be listed !!  ", (3,2))))  

def print_prompt():
   console.print(Align.left(Padding(" - What would you like to do? - ",(1,0))))

def get_choice():
   return console.input(Align.left(" Response  "))
   

# def get_terminal_size():
#     return os.get_terminal_size().columns

def print_choice():
   text = Text(" Options ")
   choice = Align.left(text)
   return print(choice)


''' Pokemon Center CLI '''


def display_welcome():
  clear()
  console.print(Align.center(Padding("Welcome to CLI Pokémon. Your adventure in the world of Pokémon begins now!" + ("\n" * 2) + "From the Main Menu, you are able to view the Region's available Pokemon," + "\n" + "and try your hand at becoming a Pokemon Master through our Trainer Area.", (3,2))))
#   text = "Welcome to CLI Pokemon. Your adventure in the world of Pokemon begins now! \n \n From the Main Menu, you are able to view the Region's available Pokemon and try your hand at becoming a Pokemon Master through our Trainer Area."
#   box = Align.center(welcome_mssg)
  two_line_space()
  enter = input("Press Enter to Begin  ")
  if len(enter) >= 0:
     while True:
        display_main_menu()
        break


def display_main_menu():
  clear()
  console.print(Align.center(Padding(" - Main Menu -  \n\n 1. Trainer Center \n 2. Pokémon Center \n 3. Exit Game", (3,3))))
  print_prompt()
  print('\n')
  print_choice()
  print("1")
  print("2")
  choice = get_choice()
  if choice == '1' or choice == '1.':
    intro_trainer_center()
  elif choice == '2' or choice == '2.':
    display_pokemon_center()
  elif choice == '3' or choice == '3.':
     SystemExit()
  else:
    clear()
    print_error()
    two_second_timer()
    display_main_menu()
  

def display_pokemon_center():
   clear()
   print(Align.center(Padding("Welcome to the Pokémon center, where you can explore the Region's pokémon!", (1,1))))
   two_line_space()
   print(Align.center(Padding(" - Pokémon Center -  \n\n 1. See Pokémon in Region \n 2. Exit to Main Menu  ")))
   two_line_space()
   print_prompt()
   print('\n')
   print("1")
   print("2")
   choice = get_choice()
   if choice == '1' or choice == '1.':
      clear()
      show_region_pokemon()
   elif choice == '2' or choice == '2.':
      clear()
      display_main_menu()
   else:
      clear()
      print_error()
      display_pokemon_center()


def show_region_pokemon():
    poke = get_all_pokemon()
    for pokemon in poke:
       print(f"ID: {pokemon.id} | {pokemon.name}")
    
    two_line_space()
    console.print(Align.center(Padding(" - Pokémon - ", (2,2))))
    console.print(Align.center(Padding("1. View Pokémon Details \n2. Exit to Main Menu", (2,2))))
    print('\n')
    print_choice()
    print(' 1 \n 2')
    choice = get_choice()
    if choice == '1' or choice == '1.':
       poke_id = input("What is the ID of the Pokémon you'd like to see?   ")
       display_pokemon_details(poke_id)
    elif choice == '2' or choice == '2.':
       clear()
       display_main_menu()
    else:
       clear()
       print_error()
       one_second_timer()
       clear()
       show_region_pokemon()


def display_pokemon_details(poke_id):
   clear()
   pokemon_details = get_pokemon_by_id(poke_id)
   if not pokemon_details:
      print(f"!!! No Pokémon were found with the ID of {poke_id} !!!")
      two_second_timer()
      show_region_pokemon()
   else:
      two_line_space()
      print(f'Pokémon Name: {pokemon_details.name}')
      print(f'\n')
      print(f'HP - {pokemon_details.max_hp}')
      print(f'Attack - {pokemon_details.attack_name}')
      print(f'Attack Damage - {pokemon_details.attack_damage}')
      print("\n")
      owner_id = pokemon_details.trainer_id
      if not owner_id:
         print(f'This {pokemon_details.name} is currently wild!')
         four_line_space()
      else:
         print(f'This Pokémon is currently being trained by: {show_pokemon_trainer_name(owner_id)}')
      done = input("Press enter when finished")
      if len(done) >= 0:
        clear()
        two_line_space()
        display_details_menu()
      

def display_details_menu():
   print(Align.center(" - What's next? - "))
   print('\n')
   print(Align.center("1. See all Region Pokémon. \n2. Exit to Main Menu. \n3. Return to Pokémon Center."))
   four_line_space()
   choice = get_choice()
   if choice == '1' or choice == '1.':
      show_region_pokemon()
   elif choice == '2' or choice == '2.':
      display_main_menu()
   elif choice == '3' or choice == '3.':
      display_pokemon_center()
   else:
        clear()
        print_error()
        two_second_timer()
        clear()
        display_details_menu()
     
''' Variables or Functions specifically for Trainer Center '''




''' Trainer Center CLI '''

def intro_trainer_center():
   clear()
   console.print(Align.center(Padding(" Welcome to CLIPokémon's Trainer Center! ", (2,4))))
   two_line_space()
   console.print(Align.center(Padding("Here you will embark on your journey to becoming the next great Pokémon trainer. \n When you are ready, choose your trainer and start a battle!")))
   four_line_space()


   choice = input("Press Enter..")
   if len(choice) >= 0:
      display_trainer_center_menu()

def display_trainer_center_menu():
   clear()
   console.print(Align.center(Padding(' - Trainer Center - ', (3,2))))
   console.print(Align.center('1. See All Trainers \n2. Create New Trainer \n3. Enter Battle Arena \n4. Return to Main Menu'))
   four_line_space()

   print_choice()
   print(' 1 \n 2 \n 3 \n 4')
   choice = get_choice()
   if choice == '1':
      display_all_trainers()
      '''def handle all_display_response()'''
   elif choice == '2':
      intro_create_trainer()
   elif choice == '3':
      intro_choose_trainer()
      '''def select_trainer()'''
   elif choice == '4':
      display_main_menu()
   else:
      clear()
      print_error()
      two_second_timer()
      display_trainer_center_menu()

''' Trainer Center Menu Option 1''' 

def display_all_trainers():
   clear()
   trainers = get_all_trainers()
   trainer_ids = []
   two_line_space()
   console.print(Align.left(Padding(' - Current Trainers - ', (2,2))))
   for trainer in trainers:
      trainer_ids.append(trainer.id)
      console.print(Align.left(Padding(f"ID: {trainer.id} | {trainer.name} | age: {trainer.age}")))
   two_line_space()
   trainer_display_options(trainer_ids)

def trainer_display_options(trainer_ids):
   ids = trainer_ids
   console.print(Align.center(Padding(" - What's Next? - ", (2,2))))
   console.print(Align.center(Padding("1. View Trainer Details \n2. Delete a Trainer \n3. Return to Trainer Center", (2,2))))
   two_line_space()
   print_choice()
   print(' 1 \n 2 \n 3')
   choice = get_choice()
   if choice == '1':
      inner_choice = input("What is the ID of the trainer you'd like to see?  ")
      if inner_choice == '' or int(inner_choice) not in ids:
         clear()
         print_error()
         two_second_timer()
         display_all_trainers()
      else:
         display_trainer_details(inner_choice)
   elif choice == '2':
      inner_choice = input("What is the ID of the Trainer that you would like to drop?")
      if inner_choice  == '' or int(inner_choice) not in ids:
         clear()
         print_error()
         two_second_timer()
         display_all_trainers()
      else:
         clear()
         handle_delete_trainer(inner_choice)
         console.print(Align.center(Padding(" The Trainer sailed off into the distance... ", (2,2))))
         two_second_timer()
         display_all_trainers()
   elif choice == '3':
      display_trainer_center_menu()
   else:
      clear()
      print_error()
      two_second_timer()
      display_all_trainers()

def display_trainer_details(trainer_id):
   clear()
   trainer = get_trainer_by_id(trainer_id)
   two_line_space()
   console.print(Align.center(Padding(f"Trainer Name:  {trainer.name} \nAge:  {trainer.age} \nMotto:  {trainer.motto}", (2,3))))
   
   two_line_space()
   console.print(Align.center(Padding(" - What's next? - ", (2,2))))
   console.print(Align.center(Padding("1. See All Trainers \n2. Exit to Trainer Center", (2,2))))
   two_line_space()
   print_choice()
   print(" 1 \n 2")
   
   choice = get_choice()
   if choice == '1':
      display_all_trainers()
   elif choice == '2':
      display_trainer_center_menu()
   else:
      clear()
      print_error()
      two_second_timer()
      display_trainer_details(trainer_id)
      
''' Trainer Center Menu Option 2'''

def intro_create_trainer():
   clear()
   console.print(Align.center(Padding("I'm happy to hear that you beginning your Pokémon Master journey! \n\n Let's start by getting to know you!.", (3,2))))
   two_line_space()
   ready = input("Enter...")
   if len(ready) >= 0:
      create_new_trainer()
   else:
      intro_create_trainer()

def create_new_trainer():
   clear()
   console.print(Align.center(Padding('What is your name?', (3,3))))
   two_line_space()
   name = get_choice()
   if len(name) >= 1:
      get_new_trainer_age(name)
   else:
      clear()
      console.print(Align.center(Padding('Please enter a valid name!', (3,3))))
      two_second_timer()
      create_new_trainer()
   
def get_new_trainer_age(name):
   clear()
   console.print(Align.center(Padding(f"Well hello, {name}! We are happy to have you! \n \n How old are you?", (3,3))))
   two_line_space()
   age = get_choice()
   if age == '' or int(age) < 1:
      clear()
      console.print(Align.center(Padding('Please enter a valid age!', (3,3))))
      two_second_timer()
      get_new_trainer_age(name)
   else:
    get_new_trainer_motto(name, age)

def get_new_trainer_motto(name, age):
   clear()
   console.print(Align.center(Padding(f"{name}, with your life expereince I am sure that you will make an excellent Pokémon Trainer! \nOne final thing...we all have our own little catch phrase around here... \nWhat would your motto be?", (3,3))))
   two_line_space()
   new_motto = get_choice()
   if len(new_motto) >= 2:
      add_trainer_to_table(name, age, new_motto)
      display_all_trainers()
   else:
      clear()
      console.print(Align.center(Padding('Come on...everyone loves a catchphrase..', (3,3))))
      two_second_timer()
      get_new_trainer_motto(name, age)

''' Trainer Center Menu Option 3'''

def intro_choose_trainer():
   clear()
   console.print(Align.center(Padding("Below is a list of all available Trainers! \nChoose your Trainer by entering their ID below!", (3,2))))
   two_line_space()
   trainers = get_all_trainers()
   trainer_ids = []

   for trainer in trainers:
      trainer_ids.append(trainer.id)
      print(f"ID: {trainer.id} | {trainer.name}")
   two_line_space()

   choice = get_choice()
   if choice == '' or int(choice) not in trainer_ids:
      clear()
      print_error()
      two_second_timer()
      intro_choose_trainer()
   else:
      display_battle_menu(choice)
      
""" Battle CLI """
def display_battle_menu(input_choice):
   clear()
   trainer = get_trainer_by_id(input_choice)
   pokemon = get_trainers_pokemon(trainer.id)
   console.print(Align.center(Padding(f"Welcome, {trainer.name}, to the Battle Arena! \n Here you can view and manage your team, and start a Battle!")))
   two_line_space

   console.print(Align.center(Padding(' - Battle Arena - ', (1,1))))
   console.print(Align.center(Padding(f"1. See {trainer.name}'s Pokemon \n2. Battle \n3. Exit to Trainer Menu",(1,1))))
   console.print('\n')
   print_choice()
   console.print(' 1 \n 2 \n 3')
   choice = get_choice()
   if choice == '1':
      see_team_menu(pokemon, trainer)
   elif choice == '2':
      start_battle(trainer)
   elif choice == '3':
      display_trainer_center_menu()
   else:
      clear()
      print_error()
      two_second_timer()
      display_battle_menu(input_choice)
      
''' Battle Arena Menu Option 1 '''



def show_trainers_pokemon(pokemon, trainer):
   two_line_space()
   console.print(Align.center(Padding(f" - {trainer.name}'s Current Pokemon - ")))
   two_line_space()
   for poke in pokemon:
      console.print(Align.center(Padding(f"{poke.id} | {poke.name}", (1,1))))
    
def see_team_menu(pokemon, trainer):
    clear()
    show_trainers_pokemon(pokemon, trainer)
    two_line_space()
    console.print(Align.center(" - What would you like to do? -"))
    console.print(Align.center("1. Remove Pokémon from team \n2. Add Pokémon to Team \n3. Exit to Battle Arena"))
    print('\n')
    print_choice()
    print(" 1 \n 2 \n 3")
    choice = get_choice()
    if choice == '1':
       poke_select_remove(pokemon, trainer)
       pass
    elif choice == '2':
       poke_select_add(trainer)
    elif choice == '3':
       display_battle_menu(trainer.id)
    else:
       clear()
       print_error()
       two_second_timer()
       see_team_menu(pokemon, trainer)

'''from within - Option 1 - Release Pokemon'''
def poke_select_remove(pokemon, trainer):
   clear()
   poke_id = []
   for poke in pokemon:
      poke_id.append(str(poke.id))
   show_trainers_pokemon(pokemon, trainer)
   two_line_space
   console.print(Align.left(Padding("Please enter the ID of the Pokémon you wish to release", (1,1))))
   choice = get_choice()
   if choice not in poke_id:
      clear()
      print_error()
      two_second_timer()
      see_team_menu(pokemon, trainer)
   else:
      clear()
      handle_pokemon_release(choice)
      console.print(Align.center(Padding('The requested Pokémon was removed from your team.', (3,3))))
      three_second_timer()
      display_battle_menu(trainer.id)
    #   handle_pokemon_release()

'''from within - Option 2 - Add To Team'''

def poke_select_add(trainer):
   clear()
   two_line_space()
   avail_pokemon = get_available_pokemon()
   for poke in avail_pokemon:
      console.print(f"ID: {poke.id} | {poke.name}")
   two_line_space()
   console.print(Align.center(Padding(" - Would you like to try and catch one? -", (3,2))))
   console.print(Align.center(Padding('1. Yes \n2. Return to Battle Arena ', (2,2))))
   print('\n')
   print_choice()
   print(' 1 \n 2 ')
   choice = get_choice()
   if choice == '1':
      start_pokemon_catch(avail_pokemon, trainer)
   elif choice == '2':
      display_battle_menu(trainer.id)
   else:
      clear()
      print_error()
      two_second_timer()
      poke_select_add(trainer)

def start_pokemon_catch(avail_pokemon, trainer):
   id_list = []
   for poke in avail_pokemon:
      id_list.append(str(poke.id))
   print('\n')
   choice = input('What is the ID of the Pokemon you would like to catch?')
   if choice not in id_list:
      clear()
      print_error()
      two_second_timer()
      start_pokemon_catch(avail_pokemon, trainer)
   else:
      clear()
      handle_pokemon_add(choice, trainer.id)
      console.print(Align.center(Padding(f" Success! \n\n you have successfully added {show_pokemon_name(choice)} to your team! ", (3,3))))
      three_second_timer()
      start_battle(trainer)
   
      
''' Battle Arena Option 2 - Battle'''

def start_battle(trainer):
   clear()
   two_line_space()
   console.print(Align.center(Padding(f" {trainer.name} -- Get prepared to battle! \n\n Choose your selected Pokémon!", (2,3))))
   pokemon = get_trainers_pokemon(trainer.id)
   if len(pokemon) == 0:
      clear()
      console.print(Align.center(Padding(f"You do not have any Pokemon! You should try and catch some!", (3,3))))
      three_second_timer()
      poke_select_add(trainer)
   else:
      two_line_space()

      ids = [poke.id for poke in pokemon]
      show_trainers_pokemon(pokemon, trainer)
      # console.print(Align.center(show_trainers_pokemon(pokemon, trainer)))
      print('\n')
      choice = input("What is the ID of the Pokémon you would like to use?  ")
      if choice == '' or int(choice) not in ids:
         clear()
         print_error()
         two_second_timer()
         start_battle(trainer)
      else:
         get_wild_pokemon(trainer, int(choice))

def get_wild_pokemon(trainer, pokemon_id):
   clear()
   pokemon = get_pokemon_by_id(pokemon_id)
   two_line_space()
   console.print(Align.center(Padding(f"Nice! {pokemon.name} is a great choice! \n\n Let me see if I can find you a wild Pokémon to battle...", (4,4))))
   two_second_timer()
   two_line_space()
   console.print(Align.center(Padding("hmm....", (2,2))))
   three_second_timer()
   two_line_space()
   wild_pokemon = get_random_wild()
   console.print(Align.center(Padding(f"Of Course! {wild_pokemon.name} is the perfect match! ")))
   two_second_timer()
   intro_pokemon_in_battle(trainer, pokemon, wild_pokemon)


def intro_pokemon_in_battle(trainer, pokemon, wild_pokemon):
   clear()
   handle_add_battle(pokemon, wild_pokemon)
   console.print(Align.center(Padding("Battle Beginning...", (2,2) )))
   two_second_timer()
   console.print(Align.left(Padding(f"Trainer Name: {trainer.name} \nTrainer Pokémon: {pokemon.name} \nStarting HP: {pokemon.starting_hp}", (2,2))))
   three_second_timer()
   print('\n')
   console.print(Align.left(Padding(f"Wild Pokémon: {wild_pokemon.name} \nStarting HP: {wild_pokemon.starting_hp}", (2,2))))
   three_second_timer()
   begin_literal_battle(trainer, pokemon, wild_pokemon)

def begin_literal_battle(trainer, pokemon, wild_pokemon):
   two_line_space()

   while True:
    battle_menu(trainer, pokemon, wild_pokemon)
    trainer_attack_text(pokemon, wild_pokemon)
    two_second_timer()
    handle_wild_attack(pokemon, wild_pokemon)
    wild_attack_text(pokemon, wild_pokemon, trainer)
    two_second_timer()
   
def trainer_attack_text(pokemon, wild_pokemon):
   console.print(Align.left(Padding(f"{pokemon.name} attacked {wild_pokemon.name} with {pokemon.attack_name}", (1,1))))
   two_second_timer()
   console.print(Align.right(Padding(f"{wild_pokemon.name}'s HP was reduced to {wild_pokemon.starting_hp} ")))
   two_second_timer()


def text_for_wild(wild_pokemon, pokemon):
   console.print(Align.right(Padding(f"{wild_pokemon.name} attacked {pokemon.name} with {wild_pokemon.attack_name}")))
   two_second_timer()
   console.print(Align.left(Padding(f"{pokemon.name}'s HP was reduced to {pokemon.starting_hp}")))
   two_second_timer()
   

def wild_attack_text(pokemon, wild_pokemon, trainer):
   if pokemon.starting_hp <= 0:
      pokemon.starting_hp = 0
   text_for_wild(wild_pokemon, pokemon)
   three_second_timer()
   handle_battle_loss(pokemon)
      

def battle_menu(trainer, pokemon, wild_pokemon):
   poke_attack_damage = pokemon.attack_damage
   console.print(Align.center(Padding(f"- What would you like to do? -\n 1. Attack\n 2. Run")))
   choice = get_choice()
   if choice == '2':
      handle_reset_pokemon(wild_pokemon)
      run_away()
   elif choice == '1':
      reduce_wild_hp(wild_pokemon, poke_attack_damage)
      if wild_pokemon.starting_hp <= 0:
         wild_pokemon.starting_hp = 0
         trainer_attack_text(pokemon, wild_pokemon)
         two_second_timer()
         handle_battle_win(trainer, pokemon, wild_pokemon)
         
def handle_wild_attack(pokemon, wild_pokemon):
   reduce_trainer_pokemon(pokemon, wild_pokemon.attack_damage)
   console.print(Align.right(Padding(f"{wild_pokemon.name} attacked {pokemon.name} with {wild_pokemon.attack_name}")))

def handle_battle_win(trainer, pokemon, wild_pokemon):
   clear()
   console.print(Align.center(Padding(f"I knew you could do it!" , (2,2))))
   one_second_timer()
   console.print(Align.center(Padding(f"{wild_pokemon.name} did not stand a chance against your {pokemon.name}!", (2,2))))
   three_second_timer()
   console.print(Align.center(Padding(f"See you next time, {trainer.name}")))
   two_second_timer()
   handle_reset_pokemon(wild_pokemon)
   display_trainer_center_menu()
   
def handle_battle_loss(pokemon):
   clear()
   console.print(Align.center(Padding(f"Oh no...Your {pokemon.name} didn't win..\n\n When Pokémon reach 0 HP they must be treated.", (3,3))))
   handle_pokemon_release(pokemon.id)
   handle_reset_pokemon(pokemon)
   three_second_timer()
   clear()
   console.print(Align.center(Padding(f"Your pokemon {pokemon.name} was healed and released back to the wild. \n\nCatch it again for another chance!", (3,3))))
   three_second_timer()
   display_trainer_center_menu()
   
def run_away():
   one_second_timer()
   clear()
   console.print(Align.center(Padding('You got away safely...\n\nMaybe next time...')))
   three_second_timer()
   display_trainer_center_menu()


      

