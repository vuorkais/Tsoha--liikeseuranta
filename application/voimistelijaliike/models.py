from application import db
  
class VoimistelijaLiike(db.Model):
    voimistelija_id = db.Column(db.Integer, db.ForeignKey('voimistelija.id'),
        nullable=False)
    liike_id = db.Column(db.Integer, db.ForeignKey('liike.id'),
        nullable=False)