from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

#liitostaulu
voimistelijaliike = db.Table("voimistelijaliike", 
    db.Column("voimistelija_id", db.Integer, db.ForeignKey("voimistelija.id"), primary_key=True),
    db.Column("liike_id", db.Integer, db.ForeignKey("liike.id"), primary_key=True)
)

class Voimistelija(Base):

    nimi = db.Column(db.String(144), nullable=False)

    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)
    ryhma_id = db.Column(db.Integer, db.ForeignKey("ryhma.id"), nullable=False)
    liikkeet = db.relationship('Liike', secondary=voimistelijaliike,
        backref=db.backref('voimistelijat'), lazy = 'dynamic')

    def __init__(self, nimi):
        self.nimi = nimi

    @staticmethod
    def ryhman_poisto(id):
        stmt = text("UPDATE Voimistelijat SET Ryhma_id = '1' WHERE Ryhma_id = id")
        res = db.engine.execute(stmt)


	