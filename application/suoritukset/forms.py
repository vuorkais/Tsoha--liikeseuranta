from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, DateField

class SuoritusForm(FlaskForm):
    tehtyja = IntegerField("Tehtyjen määrä", [validators.NumberRange(min=0, max=None, message="Tehtyjen määrä ei voi olla negatiivinen!")])
    onnistuneita = IntegerField("Onnistuneiden määrä", [validators.NumberRange(min=0, max=None, message="Onnistuneiden määrä ei voi olla negatiivinen!")])
    harjoituskerta = DateField("Päivämäärä (muodossa YYYY-MM-DD)")
    muuta = StringField("Muuta")
 
    class Meta:
        csrf = False