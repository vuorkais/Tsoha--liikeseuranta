from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class Ryhma(Base):

    ryhma = db.Column(db.String(144), nullable=False)
    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)

    def __init__(self, ryhma, vastuuvalmentaja_id):
        self.ryhma = ryhma
        self.vastuuvalmentaja_id = vastuuvalmentaja_id

    