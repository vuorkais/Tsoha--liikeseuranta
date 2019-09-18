from application import app, db
from flask import render_template, redirect, request, url_for
from application.voimistelijat.models import Voimistelija
from application.voimistelijat.forms import TaskForm

@app.route("/voimistelijat", methods=["GET"])
def voimistelijat_index():
    return render_template("voimistelijat/list.html", voimistelijat = Voimistelija.query.all())

@app.route("/voimistelijat/uusi/")
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html", form = TaskForm())

@app.route("/voimistelijat/<voimistelija_id>/", methods=["POST"])
def voimistelijat_set_ryhma(voimistelija_id):

    v = Voimistelija.query.get(voimistelija_id)
    v.ryhma = "Topteam"
    db.session().commit()
  
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/", methods=["POST"])
def voimistelijat_create():
    form = VoimistelijaForm(request.form)

    v = Voimistelija(form.nimi.data)
    v.ryhma = form.ryhma.data
    
    return redirect(url_for("voimistelijat_index"))
