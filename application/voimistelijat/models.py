from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

#liitostaulu
VoimistelijaLiike = db.Table("voimistelijaliike", 
    db.Column("voimistelija_id", db.Integer, db.ForeignKey("voimistelija.id")),
    db.Column("liike_id", db.Integer, db.ForeignKey("liike.id"))
)

class Voimistelija(Base):

    nimi = db.Column(db.String(144), nullable=False)

    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)
    ryhma_id = db.Column(db.Integer, db.ForeignKey("ryhma.id"), nullable=False)
    voimistelijaliike = db.relationship('Liike', secondary= voimistelijaliike, lazy = 'subquery',
        backref= db.backref('voimistelijat', lazy= True))

    def __init__(self, nimi):
        self.nimi = nimi




	