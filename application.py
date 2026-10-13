from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

import os
from pathlib import Path

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    data_dir = Path(os.getenv("DATA_DIR", "instance"))
    data_dir.mkdir(parents=True, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{(data_dir / 'data.db').resolve()}"
    )

db = SQLAlchemy(app)



class Drink(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True, nullable=False)
    description=db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name}-{self.description}"
@app.route('/')
def index():
    return "Hello!"



@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []

    for drink in drinks:
        drink_data = {
            'name': drink.name,
            'description': drink.description
        }
        output.append(drink_data)

    return {"drinks": output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink=db.session.get(Drink, id)
    if drink is None:
        from flask import abort
        abort(404)
    return {"name": drink.name, "description":drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Request body must be a JSON object"}, 400

    name = data.get('name')
    description = data.get('description')

    if not isinstance(name, str) or not name.strip():
        return {"error": "A non-empty name is required"}, 400

    if description is not None and not isinstance(description, str):
        return {"error": "Description must be a string"}, 400

    drink = Drink(
        name=name.strip(),
        description=description
    )

    try:
        db.session.add(drink)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {"error": "Could not create drink; the name may already exist"}, 409

    return {'id': drink.id}, 201


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink=db.session.get(Drink, id)
    if drink is None:
        return {"error":"not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"yeeeeeeeeet"}
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=False)

