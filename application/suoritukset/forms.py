from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, DateField

class SuoritusForm(FlaskForm):
    tehtyja = IntegerField("Tehtyjen määrä", [validators.NumberRange(min=0, max=100, message="Tehtyjen määrä on liian pieni tai suuri!")])
    onnistuneita = IntegerField("Onnistuneiden määrä", [validators.NumberRange(min=0, max=100, message="Onnistuneiden määrä on liian pieni tai suuri!")])
    harjoituskerta = DateField("Päivämäärä (muodossa YYYY-MM-DD)")
    muuta = StringField("Muuta")
 
    class Meta:
        csrf = False