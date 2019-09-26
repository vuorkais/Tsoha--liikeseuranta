from application import db
from application.models import Base

class Voimistelija(Base):

    nimi = db.Column(db.String(144), nullable=False)
    ryhma = db.Column(db.String(144), nullable=False)
    
    vastuuvalmentaja_id = db.Column(db.Integer, db.ForeignKey('vastuuvalmentaja.id'), nullable=False)
	
    def __init__(self, nimi, ryhma):
        self.nimi = nimi
        self.ryhma = ryhma
