from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class Ryhma(Base):

    ryhma = db.Column(db.String(144), nullable=False)
    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)
    voimistelijat = db.relationship("Voimistelija", cascade="all, delete-orphan")

    def __init__(self, ryhma, vastuuvalmentaja_id):
        self.ryhma = ryhma
        self.vastuuvalmentaja_id = vastuuvalmentaja_id

    @staticmethod
    def listaa_ryhmat():
        stmt = text("SELECT Ryhma.id, Ryhma.ryhma FROM Ryhma")
        res = db.engine.execute(stmt).fetchall()
        response = []
        #response.append(("-1", "Tyhjä"))
        for row in res:
            response.append((row["id"], row["ryhma"]))
        return response  