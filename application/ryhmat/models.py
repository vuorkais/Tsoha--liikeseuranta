from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy

class Ryhma(Base):

    ryhma = db.Column(db.String(144), nullable=False)

    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)

    def __init__(self, ryhma):
        self.ryhma = ryhma
