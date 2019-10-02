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
    def listaa_bhaki():
        stmt = text("SELECT Vastuuvalmentaja.id, Vastuuvalmentaja.name FROM Vastuuvalmentaja"
                    " LEFT JOIN Voimistelija ON Voimistelija.vastuuvalmentaja_id = Vastuuvalmentaja.id"
                    " WHERE (Voimistelija.ryhma = :b)"
                    " GROUP BY Vastuuvalmentaja.id").params(b='B-haki')
                    #" HAVING COUNT(Voimistelija.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response