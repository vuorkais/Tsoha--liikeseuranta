from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.liikkeet.models import Liike
from application.liikkeet.forms import LiikeForm

@app.route("/liikkeet", methods=["GET"])
def liikkeet_index():
    return render_template("liikkeet/list.html", liikkeet = Liike.query.all())

@app.route("/liikkeet/uusi/")
@login_required
def liikkeet_form():
    return render_template("liikkeet/uusi.html", form = LiikeForm())

@app.route("/liikkeet/", methods=["POST"])
@login_required
def liikkeet_create():
    form = LiikeForm(request.form)
    
    if not form.validate():
        return render_template("liikkeet/uusi.html", form = form)
    
    l = Liike(form.nimi.data,form.teline.data,form.vaikeusarvo.data,form.kuvaus.data)
    
    db.session().add(l)
    db.session().commit()
    
    return redirect(url_for("liikkeet_index"))
