from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, DateField

class SuoritusForm(FlaskForm):
    tehtyja = IntegerField("Tehtyjen määrä", [validators.])
    nimi = StringField("Voimistelijan nimi", [validators.Length(min=2, max=144, message="Nimi on liian lyhyt tai pitkä!")])
    ryhma = StringField("Voimistelijan ryhmä", [validators.Length(min=2, max=144, message="Ryhmän nimi on liian lyhyt tai pitkä!")])
 
    class Meta:
        csrf = False