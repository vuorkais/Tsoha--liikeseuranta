from flask import render_template
from application import app
from application.liikkeet.models import Liike
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html")
    #telineena_puomi=Liike.etsi_puomiliikkeet(), bhaki_valkku=User.listaa_bhaki()
