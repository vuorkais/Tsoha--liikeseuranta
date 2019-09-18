from flask_wtf import FlaskForm
from wtforms import StringField, validators

class VoimistelijaForm(FlaskForm):
    nimi = StringField("Voimistelijan nimi", [validators.Length(min=2)])
    ryhma = StringField("Voimistelijan ryhmä", [validators.Length(min=2)])
 
    class Meta:
        csrf = False
