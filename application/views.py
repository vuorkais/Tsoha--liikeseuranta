from application import app, db
from flask import render_template, request
from application.voimistelijat.models import Voimistelija

@app.route("/voimistelijat/uusi/")
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html")

@app.route("/voimistelijat/", methods=["POST"])
def voimistelijat_create():
    v = Voimistelija(request.form.get("nimi", "ryhma"))

    db.session().add(v)
    db.session().commit()
    
    return "hei maailma!"
