from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "vastuuvalmentaja"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    voimistelijat = db.relationship("Voimistelija", backref='vastuuvalmentaja', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def listaa_valmentajia_r():
        stmt = text("SELECT Vastuuvalmentaja.id, Vastuuvalmentaja.name, COUNT(Ryhma.id) AS ryhmat FROM Vastuuvalmentaja"
                    " LEFT JOIN Ryhma ON Ryhma.vastuuvalmentaja_id = Vastuuvalmentaja.id"
                    " GROUP BY Vastuuvalmentaja.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "ryhmat":row[2]})

        return response

    @staticmethod
    def listaa_valmentajia_v():
        stmt = text("SELECT Vastuuvalmentaja.id, Vastuuvalmentaja.name, COUNT(Voimistelija.id) AS voimistelijat FROM Vastuuvalmentaja"
                    " LEFT JOIN Voimistelija ON Voimistelija.vastuuvalmentaja_id = Vastuuvalmentaja.id"
                    " GROUP BY Vastuuvalmentaja.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "voimistelijat":row[2]})

        return response