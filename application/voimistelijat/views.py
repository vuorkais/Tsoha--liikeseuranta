from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.voimistelijat.models import Voimistelija
from application.voimistelijat.forms import VoimistelijaForm, LisaaLiikeForm, VoimistelijanRyhmaForm
from application.ryhmat.models import Ryhma
from application.liikkeet.models import Liike
from application.ryhmat.forms import RyhmaForm

@app.route("/voimistelijat", methods=["GET"])
def voimistelijat_index():
    return render_template("voimistelijat/list.html", voimistelijat = Voimistelija.query.all())

@app.route("/voimistelijat/<voimistelija_id>/remove", methods=["POST"])
@login_required
def voimistelijat_remove(voimistelija_id):

    v = Voimistelija.query.get(voimistelija_id)
    
    db.session().delete(v)
    db.session().commit()
  
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/<ryhma_id>/lisataan", methods=["POST"])
@login_required
def voimistelijat_lisaa(ryhma_id):

    form = VoimistelijaForm(request.form)
    ryhma = ryhma_id
    if not form.validate():
        return render_template("voimistelijat/uusi.html", form = form, ryhma_id= ryhma)
    
    v = Voimistelija(form.nimi.data)
    v.vastuuvalmentaja_id = current_user.id
    v.ryhma_id = ryhma
    
    db.session().add(v)
    db.session().commit()
    
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/<voimistelija_id>/lisaaliike", methods=["POST"])
@login_required
def lisaa_liike_voimistelijalle(voimistelija_id):

    voimistelija_id = voimistelija_id
#    v = db.session.query(Voimistelija).get(voimistelija_id)
#    voimistelija_liikkeet = voimistelija.listaa_liikkeet()
    form = LisaaLiikeForm()
    form.liike.choices = Liike.listaa_liikkeet()
    
    if not form.validate():
        return render_template("voimistelijat/uusiliike.html", form = form, voimistelija_id= voimistelija_id)
#    form.liike.choices = Liike.listaa_liikkeet()
#    form.liikevaihtoehdot = Voimistelija.listaa_liikkeet()
#    if not form.validate():
#    return render_template("voimistelijat/uusiliike.html", form = form, voimistelija_id= voimistelija_id)
    
#    l = Liike(form.id.data)
    return redirect(url_for("voimistelijat_index"))

@app.route("/voimistelijat/<voimistelija_id>/paivitys", methods=["POST"])
@login_required
def paivita_ryhma(voimistelija_id):

    voimistelija_id = voimistelija_id
    form = VoimistelijanRyhmaForm()
    form.ryhma.choices = Ryhma.listaa_ryhmat()

    if not form.validate():
        return render_template("voimistelijat/uusiryhma.html", form = form, voimistelija_id= voimistelija_id)
    
    #v = Voimistelija.query.get(voimistelija_id)    
    #form.ryhma.data
    #Tähän valitaan se ryhmän id, jonka nimi on valittu choices-listasta

    #db.session().update(v)
    #db.session().commit()
    
    return redirect(url_for("voimistelijat_index"))