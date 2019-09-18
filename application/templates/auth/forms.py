from flask_wtf import VoimistelijaForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False
