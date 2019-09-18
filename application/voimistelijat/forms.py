from flask_wtf import FlaskForm
from wtforms import StringField, validators

class VoimistelijaForm(FlaskForm):
    nimi = StringField("Voimistelijan nimi", [validators.Length(min=2, max=144, message="Syöte on väärän pituinen!")])
    ryhma = StringField("Voimistelijan ryhmä", [validators.Length(min=2, max=144, message="Syöte on väärän pituinen!")])
 
    class Meta:
        csrf = False
