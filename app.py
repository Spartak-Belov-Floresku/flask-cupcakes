from flask import Flask, jsonify, request, render_template

from models import db, connect_db, Cupcake
from forms import CupcakeForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://admin_flask:password@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = 'helloworld'
app.debug = True

@app.route('/')
def home_page():
    form = CupcakeForm()
    return render_template('index.html', form=form)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():

    request_json = request.get_json()
    req = request_json['json']

    flavor = req.get('flavor', 'Vanilla')
    size = req.get('size')
    rating = req.get('rating')
    image = req.get('image')

    if not image:
        image = 'https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg'

    cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image
    )

    db.session.add(cupcake)
    db.session.commit()
    
    json_resp = jsonify(cupcake=cupcake.serialize())

    return (json_resp, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', 'vanilla')
    cupcake.size = request.json.get('size', 'medium')
    cupcake.rating = request.json.get('rating', 10)
    cupcake.image = request.json.get('image')

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')


@app.route('/api/cupcakes/find')
def find_cupcakes():
    
    search = request.args.get('find')
    results = Cupcake.query.filter(Cupcake.flavor.ilike(f'%{search}%'))
    all_cupcakes = [result.serialize() for result in results]
    return jsonify(cupcakes=all_cupcakes)
    


if __name__ == "__main__":
    app.run(debug=True)