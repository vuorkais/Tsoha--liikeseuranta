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
    def listaa_liikkeet():
        stmt = text("SELECT Liike.id, Liike.nimi, Liike.teline  FROM Liike")
        res = db.engine.execute(stmt).fetchall()
        response = []
        response.append(("Tyhjä", "Tyhjä"))
        for row in res:
            response.append((row["id"], row["nimi"]))
        return response
    
    @staticmethod
    def listaa_ryhman_liikkeet(ryhma_id):
        stmt = text("SELECT Liike.nimi AS Liike, Liike.teline AS Teline, Liike.vaikeusarvo AS Vaikeus FROM Liike"
                    " INNER JOIN VoimistelijaLiike ON VoimistelijaLiike.liike_id = Liike.id"
                    " INNER JOIN Voimistelija ON Voimistelija.id= VoimistelijaLiike.voimistelija_id"
                    " INNER JOIN Ryhma ON Ryhma.id= Voimistelija.ryhma_id"
                    " WHERE Ryhma.id= :ryhma_id"
                    " GROUP BY Liike.nimi").params(ryhma_id=1)

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"liike":row[0], "teline":row[1], "vaikeus":row[2]})
        return response