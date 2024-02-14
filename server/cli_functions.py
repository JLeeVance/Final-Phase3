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
   print(" - What would you like to do? - ")

def get_choice():
   return input("Response:     ")

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
  console.print(Align.center(Padding(" - Main Menu -  \n\n 1. Trainer Center \n 2. Pokémon Center  ", (3,3))))
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
       print(f"{pokemon.id} | {pokemon.name}")
    
    two_line_space()
    print(Align.left(" - Pokémon - "))
    print("1. View Pokémon Details \n2. Exit to Main Menu")
    print('\n')
    print_choice()
    print('1 \n2')
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
   '''need to account for wrong entry'''
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
      if pokemon_details.trainer_id:
        owner_id = pokemon_details.trainer_id
        print(f'This Pokémon is currently being trained by: {show_pokemon_trainer_name(owner_id)}')
        four_line_space()
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
   console.print(Align.center('1. See All Trainers \n2. Create New Trainer \n3. Choose Your Trainer \n4. Return to Main Menu'))
   four_line_space()

   print_choice()
   print('1 \n2 \n3 \n4')
   choice = get_choice()
   if choice == '1':
      display_all_trainers()
      '''def handle all_display_response()'''
   elif choice == '2':
      intro_create_trainer()
      pass
   elif choice == '3':
      intro_choose_trainer()
      '''def select_trainer()'''
   elif choice == '4':
      display_main_menu()
   else:
      clear()
      print_error
      two_second_timer()
      display_trainer_center_menu()

''' Trainer Center Menu Option 1''' 

def display_all_trainers():
   clear()
   trainers = get_all_trainers()
   for trainer in trainers:
      print(f"{trainer.id} | {trainer.name} | age: {trainer.age}")
   two_line_space()
   trainer_display_options()

def trainer_display_options():
   console.print(Align.left(" - What's Next? - "))
   print("1. View Trainer Details \n2. Return to Trainer Center")
   two_line_space()
   print_choice()
   print('1 \n2')
   choice = get_choice()
   if choice == '1':
      inner_choice = input("What is the ID of the trainer you'd like to see?  ")
      display_trainer_details(inner_choice)
   elif choice == '2':
      display_trainer_center_menu()
   else:
      print_error()

def display_trainer_details(trainer_id):
   clear()
   trainer = get_trainer_by_id(trainer_id)
   console.print(Align.center(Padding(f"Trainer Name:  {trainer.name} \nAge:  {trainer.age} \nMotto:  {trainer.motto}", (2,3))))
   
   two_line_space()
   console.print(Align.left(" - What's next? - "))
   console.print(Align.left(Padding("1. See All Trainers \n2. Exit to Trainer Center")))
   two_line_space()
   print_choice()
   print("1 \n2")
   
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

def create_new_trainer():
   clear()
   console.print(Align.center(Padding('What is your name?', (3,3))))
   two_line_space()
   name = get_choice()
   if len(name) >= 1:
      get_new_trainer_age(name)
   else:
      create_new_trainer()
   
def get_new_trainer_age(name):
   clear()
   console.print(Align.center(Padding(f"Well hello, {name}! We are happy to have you! \n \n How old are you?")))
   two_line_space()
   age = get_choice()
   if len(age) >= 1 and len(age) < 3:
    get_new_trainer_motto(name, age)
   else:
      get_new_trainer_age()

def get_new_trainer_motto(name, age):
   clear()
   console.print(Align.center(Padding(f"{name}, with your life expereince I am sure that you will make an excellent Pokémon Trainer! \nOne final thing...we all have our own little catch phrase around here... \nWhat would your motto be?", (3,2))))
   two_line_space()
   new_motto = get_choice()
   if len(new_motto) >= 2:
      add_trainer_to_table(name, age, new_motto)
      display_all_trainers()
   else:
      get_new_trainer_motto()

''' Trainer Center Menu Option 3'''

def intro_choose_trainer():
   clear()
   console.print(Align.center(Padding("Below is a list of all available Trainers! \nChoose your Trainer by entering their ID below!", (3,2))))
   two_line_space()
   trainers = get_all_trainers()
#    print(trainers)
   for trainer in trainers:
      print(f"{trainer.id} | {trainer.name}")
   two_line_space()

#    print_choice()
#    print("1 - Trainer's ID \n2. Return to the Trainer Center")
   choice = get_choice()
   if int(choice) in range(1 , get_trainer_count()):
      display_battle_menu(choice)
   else:
      intro_choose_trainer()
      

def display_battle_menu(choice):
   clear()
   trainer = get_trainer_by_id(choice)
   pokemon = get_trainers_pokemon(trainer.id)
   console.print(Align.center(Padding(f"Welcome, {trainer.name}, to the Battle Arena! \n Here you can view and manage your team, and start a Battle!")))
   two_line_space

   console.print(Align.left(Padding(' - Battle Arena - ', (1,1))))
   console.print(f"1. See {trainer.name}'s Pokemon \n2. Battle \n3. Exit to Trainer Menu")
   console.print('\n')
   print_choice()
   console.print('1 \n2 \n3')
   choice = get_choice()
   if choice == '1':
      see_team_menu(pokemon, trainer)
   elif choice == '2':
      pass
   elif choice == '3':
      display_trainer_center_menu()
   else:
      clear()
      print_error()
      two_second_timer()
      display_battle_menu(choice)
      
''' Battle Arena Menu Option 1 '''



def show_trainers_pokemon(pokemon, trainer):
   clear()
   two_line_space()
   console.print(Align.center(Padding(f" - {trainer.name}'s Current Pokemon - ")))
   two_line_space()
   for poke in pokemon:
      console.print(Align.left(Padding(f"{poke.id} | {poke.name}", (1,1))))
    
def see_team_menu(pokemon, trainer):
    clear()
    show_trainers_pokemon(pokemon, trainer)
    two_line_space()
    console.print(Align.left(" - What would you like to do? -"))
    console.print(Align.left("1. Remove Pokémon from team \n2. Add Pokémon to Team \n3. Exit to Battle Arena"))
    print('\n')
    print_choice()
    print("1 \n2 \n3")
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
   console.print("Please enter the ID of the Pokémon you wish to release")
   choice = get_choice()
   if choice not in poke_id:
      clear()
      print_error()
      two_second_timer()
      see_team_menu(pokemon, trainer)
   else:
      clear()
      handle_pokemon_release(choice)
      console.print(Align.center(Padding('The requested Pokémon was removed from your team.', (3,2))))
      three_second_timer()
      display_battle_menu(trainer.id)
    #   handle_pokemon_release()

'''from within - Option 2 - Add To Team'''

def poke_select_add(trainer):
   clear()
   two_line_space()
   avail_pokemon = get_available_pokemon()
   for poke in avail_pokemon:
      console.print(f"{poke.id} | {poke.name}")
   two_line_space()
   console.print(Align.center(Padding(" - Would you like to try and catch one? -", (3,2))))
   console.print(Align.left(Padding('1. Yes \n2. Return to Battle Arena ')))
   print('\n')
   print_choice()
   print('1 \n2 ')
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
      console.print(Align.center(Padding(f" Success! \n\n you have successfully added {show_pokemon_name(choice)} to your team! ")))
      three_second_timer()
      display_battle_menu(trainer.id)
   
      

   
    
