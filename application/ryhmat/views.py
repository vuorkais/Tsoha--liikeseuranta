from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user, login_manager

from application import app, db
from application.ryhmat.models import Ryhma
from application.ryhmat.forms import RyhmaForm

@app.route("/ryhmat", methods=["GET"])
def ryhmat_index():
    return render_template("ryhmat/list.html", ryhmat = Ryhma.query.all())

@app.route("/ryhmat/uusi/")
@login_required
def ryhmat_form():
    return render_template("ryhmat/uusi.html", form = RyhmaForm())

@app.route("/ryhmat/", methods=["POST"])
@login_required
def ryhmat_create():
    form = RyhmaForm(request.form)
    
    if not form.validate():
        return render_template("ryhmat/uusi.html", form = form)
    
    r = Ryhma(form.ryhma.data)
    r.vastuuvalmentaja_id = current_user.id
    
    db.session().add(r)
    db.session().commit()
    
    return redirect(url_for("ryhmat_index"))

@app.route("/ryhmat/<ryhma_id>/remove", methods=["POST"])
@login_required
def ryhmat_remove(ryhma_id):

    r = Ryhma.query.get(ryhma_id)
    if r.vastuuvalmentaja_id != current_user.id:
        print("EI ole sinun ryhmä!")
        return redirect(url_for("ryhmat_index"))
    
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("ryhmat_index"))