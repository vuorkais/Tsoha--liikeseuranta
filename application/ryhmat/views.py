from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user, login_manager
from sqlalchemy import update

from application import app, db
from application.ryhmat.models import Ryhma
from application.ryhmat.forms import RyhmaForm
from application.voimistelijat.models import Voimistelija

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
    
    r = Ryhma(form.ryhma.data, vastuuvalmentaja_id = current_user.id)
    r.vastuuvalmentaja_id = current_user.id
    
    db.session().add(r)
    db.session().commit()
    
    return redirect(url_for("ryhmat_index"))

@app.route("/ryhmat/<ryhma_id>/remove", methods=["POST"])
@login_required
def ryhmat_remove(ryhma_id):

    r = Ryhma.query.get(ryhma_id)
    update(Voimistelija).where(Voimistelija.ryhma_id==ryhma_id).\
        values(ryhma_id='-1')
    
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("ryhmat_index"))