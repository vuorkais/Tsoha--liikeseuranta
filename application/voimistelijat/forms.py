from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

class VoimistelijaForm(FlaskForm):
    nimi = StringField("Voimistelijan nimi", [validators.Length(min=2, max=144, message="Nimi on liian lyhyt tai pitkä!")])
 
    class Meta:
        csrf = False

class LisaaLiikeForm(FlaskForm):
    liike = SelectField("Liike", choices=())

    class Meta:
        csrf = False
