from flask import render_template
from application import app
from application.voimistelijat.models import Voimistelija
from application.auth.models import User
from flask_login import current_user

@app.route('/')
def index():
    return render_template("index.html", listaa_valmentajia_ryhma=User.listaa_valmentajia_r(), listaa_valmentajia_voimistelija=User.listaa_valmentajia_v())
