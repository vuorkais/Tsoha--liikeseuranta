from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    name = StringField("Voimistelijan nimi")
 
    class Meta:
        csrf = False
