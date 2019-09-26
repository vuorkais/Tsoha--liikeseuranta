from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
class SigninForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144, message="Nimi on liian lyhyt tai pitkä!")])
    username = StringField("Käyttäjänimi", [validators.Length(min=2, max=20, message="Käyttäjänimi on liian lyhyt tai pitkä!")])
    password = PasswordField('Uusi salasana', [validators.InputRequired(), validators.EqualTo('confirm', message='Syötettyjen salasanojen pitää vastata toisiaan!')])
    confirm  = PasswordField('Toista salasana')

    class Meta:
        csrf = False