from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, TextAreaField

class VoimistelijaForm(FlaskForm):
    nimi = StringField("Liikkeen nimi", [validators.Length(min=2, max=144, message="Liikkeen nimi on liian lyhyt tai pitkä!")])
    teline = SelectField("Liikkeen teline", choices=[('hy', 'Hyppy'), ('no', 'Nojapuut'), ('pu', 'Puomi'), ('pe', 'Permanto')])
    vaikeusarvo = SelectField("Liikkeen vaikeusarvo", choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('muu', 'Muu')])
    kuvaus = TextAreaField("Kuvaus liikkeestä")

    class Meta:
        csrf = False
