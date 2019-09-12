from application import app
from flask import render_template, request

@app.route("/voimistelijat/uusi/")
def voimistelijat_form():
    return render_template("voimistelijat/uusi.html")

@app.route("/voimistelijat/", methods=["POST"])
def voimistelijat_create():
    print(request.form.get("nimi"))

    return "hei maailma!"
