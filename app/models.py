from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    created = db.Column(db.DateTime)

    def __repr__(self):
        return '<Product %r>' % self.name
