from config import app, migrate
from db_utils import *
from cli_functions import *
from models import db



if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)

    display_welcome()



  
