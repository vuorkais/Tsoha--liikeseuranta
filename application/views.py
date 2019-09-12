from application import app
from flask import render_template, request

@app.route("/voimistelijat/uusi/")
def tasks_form():
    return render_template("voimistelijat/uusi.html")

@app.route("/voimistelijat/", methods=["POST"])
def tasks_create():
    print(request.form.get("nimi"))
  
    return "hello world!"
