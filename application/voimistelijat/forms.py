from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    nimi = StringField("Voimistelijan nimi")
    ryhma = StringField("Voimistelijan ryhmä")
 
    class Meta:
        csrf = False
