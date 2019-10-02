from application import db
from application.models import Base
from flask_sqlalchemy import SQLAlchemy

liitostaulu_voimistelijaliike = db.Table("liitostaulu_voimistelijaliike", 
    db.Column("voimistelija_id", db.Integer, db.ForeignKey("voimistelija.id"), primary_key=True),
    db.Column("liike_id", db.Integer, db.ForeignKey("liike.id"), primary_key=True)
)

class Voimistelija(Base):

    nimi = db.Column(db.String(144), nullable=False)
    ryhma = db.Column(db.String(144), nullable=False)
    
    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)
	
    def __init__(self, nimi, ryhma):
        self.nimi = nimi
        self.ryhma = ryhma

