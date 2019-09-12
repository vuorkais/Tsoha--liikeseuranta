from application import app, db
from flask import render_template, request
from application.voimistelijat.models import Voimistelija

@app.route("/voimistelijat", methods=["GET"])
def voimistelijat_index():
    return render_template("voimistelijat/list.html", voimistelijat = Voimistelija.query.all())

@app.route("/voimistelijat/uusi/")
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html")

@app.route("/voimistelijat/", methods=["POST"])
def voimistelijat_create():
    v = Voimistelija(request.form.get("nimi"))

    db.session().add(v)
    db.session().commit()
    
    return redirect(url_for("voimistelijat_index"))
