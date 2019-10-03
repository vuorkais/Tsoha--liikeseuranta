from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.voimistelijat.models import Voimistelija
from application.voimistelijat.forms import VoimistelijaForm
from application.ryhmat.models import Ryhma
from application.ryhmat.forms import RyhmaForm
from application.liikkeet.models import Liike

@app.route("/voimistelijat", methods=["GET"])
def voimistelijat_index():
    return render_template("voimistelijat/list.html")#, voimistelijat = Voimistelija.query.all())

@app.route("/voimistelijat/<voimistelija_id>/remove", methods=["POST"])
@login_required
def voimistelijat_remove(voimistelija_id):

    v = Voimistelija.query.get(voimistelija_id)
    
    db.session().delete(v)
    db.session().commit()
  
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/lisays/")
@login_required
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html", form = VoimistelijaForm())

@app.route("/ryhmat/lisataan", methods=["POST"])
@login_required
def voimistelijat_lisaa(ryhma_id):

    form = VoimistelijaForm(request.form)
    
    if not form.validate():
        return render_template("voimistelijat/uusi.html", form = form)
    
    v = Voimistelija(form.nimi.data)
    v.vastuuvalmentaja_id = current_user.id
    v.ryhma_id = 0
    #Ryhma.query.get(ryhma_id)
    
    db.session().add(v)
    db.session().commit()
    
    return redirect(url_for("voimistelijat_index"))
