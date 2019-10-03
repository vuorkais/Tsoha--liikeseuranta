# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy

import os
# Käytetään voimistelijat.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///voimistelijat.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Ole hyvä ja kirjaudu."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# Luetaan kansiosta application tiedostojen models ja views sisältö
from application import views
from application.voimistelijat import models
from application.voimistelijat import views
from application.auth import models 
from application.auth import views 
from application.liikkeet import models
from application.liikkeet import views
from application.suoritukset import models
from application.suoritukset import views
from application.ryhmat import models
from application.ryhmat import views
from application.ryhmat.models import Ryhma

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()

Luodaan 'ryhmättömät' ryhmä
Ryhma(ryhma='Ryhmättömät', vastuuvalmentaja_id=0)
tyhja_ryhma = Ryhma(ryhma='Ryhmättömät', vastuuvalmentaja_id=0)
db.session().add(tyhja_ryhma)
db.session().commit()

