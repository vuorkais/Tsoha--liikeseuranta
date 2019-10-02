from flask_wtf import FlaskForm
from wtforms import StringField, validators

class RyhmaForm(FlaskForm):
    ryhma = StringField("Ryhmän nimi", [validators.Length(min=2, max=144, message="Ryhmän nimi on liian lyhyt tai pitkä!")])
 
    class Meta:
        csrf = False