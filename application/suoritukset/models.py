from application import db
from application.models import Base

class Suoritus(Base):

    tehtyja = db.Column(db.Integer, nullable=False)
    onnistuneita = db.Column(db.Integer, nullable=False)
    harjoituskerta = db.Column(db.Date, nullable=False)
    muuta = db.Column(db.String(144))
    
    voimistelija_id = db.Column(db.Integer, db.ForeignKey('voimistelija.id'), nullable=False)
    liike_id = db.Column(db.Integer, db.ForeignKey('liike.id'), nullable=False)
	
    def __init__(self, tehtyja, onnistuneita, harjoituskerta, muuta):
        self.tehtyja = tehtyja
        self.onnistuneita = onnistuneita
        self.harjoituskerta = harjoituskerta
        self.muuta = muuta