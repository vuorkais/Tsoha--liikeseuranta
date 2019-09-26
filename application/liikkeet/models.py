from application import db
from application.models import Base

from sqlalchemy.sql import text

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

    @staticmethod
    def etsi_puomiliikkeet():
        stmt = text("SELECT Liike.id, Liike.nimi, Liike.teline FROM Liike"
                    " WHERE (Liike.teline IS 'Puomi')"
                    " GROUP BY Liike.id")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "nimi":row[1], "teline":row[2]})

        return response