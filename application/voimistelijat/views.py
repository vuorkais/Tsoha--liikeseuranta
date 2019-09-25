from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.voimistelijat.models import Voimistelija
from application.voimistelijat.forms import VoimistelijaForm

@app.route("/voimistelijat", methods=["GET"])
def voimistelijat_index():
    return render_template("voimistelijat/list.html", voimistelijat = Voimistelija.query.all())

@app.route("/voimistelijat/uusi/")
@login_required
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html", form = VoimistelijaForm())

@app.route("/voimistelijat/<voimistelija_id>/", methods=["POST"])
@login_required
def voimistelijat_set_ryhma(voimistelija_id):

    v = Voimistelija.query.get(voimistelija_id)
    v.ryhma = "Topteam"
    db.session().commit()
  
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/", methods=["POST"])
@login_required
def voimistelijat_create():
    form = VoimistelijaForm(request.form)
    
    if not form.validate():
        return render_template("voimistelijat/uusi.html", form = form)
    
    v = Voimistelija(form.nimi.data,form.ryhma.data)
    v.vastuuvalmentaja_id = current_user.id
    
    db.session().add(v)
    db.session().commit()
    
    return redirect(url_for("voimistelijat_index"))
