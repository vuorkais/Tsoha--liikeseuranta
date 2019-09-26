from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.suoritukset.models import Suoritus
from application.suoritukset.forms import SuoritusForm

@app.route("/suoritukset", methods=["GET"])
def suoritukset_index():
    return render_template("suoritukset/list.html", suoritukset = Suoritus.query.all())

@app.route("/suoritukset/uusi/")
@login_required
def suoritukset_form():
    return render_template("suoritukset/uusi.html", form = SuoritusForm())

@app.route("/suoritukset/", methods=["POST"])
@login_required
def suoritukset_create():
    form = SuoritusForm(request.form)
    
    if not form.validate():
        return render_template("suoritukset/uusi.html", form = form)
    
    s = Suoritus(form.tehtyja.data,form.onnistuneita.data,form.harjoituskerta.data,form.muuta.data)
    s.voimistelija_id = '1'
    s.liike_id = '1'
    
    db.session().add(s)
    db.session().commit()
    
    return redirect(url_for("liikkeet_index"))