from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(25), nullable=False)
    size = db.Column(db.String(25), nullable=False)
    rating = db.Column(db.NUMERIC(precision=3, scale=1), nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg')


    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': float(self.rating),
            'image':self.image
        }


