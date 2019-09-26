from application import db
from application.models import Base

class Liike(Base):

    nimi = db.Column(db.String(144), nullable=False)
    teline = db.Column(db.String(144), nullable=False)
    vaikeusarvo = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.String(500))
	
    def __init__(self, nimi, teline, vaikeusarvo, kuvaus):
        self.nimi = nimi
        self.teline = teline
        self.vaikeusarvo = vaikeusarvo
        self.kuvaus = kuvaus