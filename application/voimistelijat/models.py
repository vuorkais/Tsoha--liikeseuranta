from application import db

class Voimistelija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    ryhma = db.Column(db.String(144), nullable=False)
	
    def __init__(self, name, ryhma):
        self.nimi = name
        self.ryhma = ryhma
