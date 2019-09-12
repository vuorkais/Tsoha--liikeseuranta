from application import app
from flask import render_template, request

@app.route("/voimistelijat/uusi/")
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html")

@app.route("/voimistelijat/", methods=["POST"])
def voimistelijat_create():
    t = Task(request.form.get("nimi"))

    db.session().add(t)
    db.session().commit()
    
    return "hei maailma!"
