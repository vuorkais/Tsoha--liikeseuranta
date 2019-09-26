from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, TextAreaField

class LiikeForm(FlaskForm):
    nimi = StringField("Liikkeen nimi", [validators.Length(min=2, max=144, message="Liikkeen nimi on liian lyhyt tai pitkä!")])
    teline = SelectField("Liikkeen teline", choices=[('Hyppy', 'Hyppy'), ('Nojapuut', 'Nojapuut'), ('Puomi', 'Puomi'), ('Permanto', 'Permanto')])
    vaikeusarvo = SelectField("Liikkeen vaikeusarvo", choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('Muu', 'Muu')])
    kuvaus = TextAreaField("Kuvaus liikkeestä")

    class Meta:
        csrf = False
