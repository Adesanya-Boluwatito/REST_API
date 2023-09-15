from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
import re
from sqlalchemy.exc import IntegrityError
import os



basedir = os.path.abspath(os.path.dirname(__file__))


# Create an instance of the Flask App
# @pytest.fixture(autouse=True)
app = Flask(__name__)

# Configure our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initializing our database
db = SQLAlchemy(app)
app.app_context().push()

class Person(db.Model):
    # __tablename__= 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)


def is_a_valid_name(name):
    return isinstance(name, str) and bool(re.match(r'^[A-Za-z\s]+$', name))

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    if "name" in data and is_a_valid_name(data["name"]):
        new_individual = Person(id=data.get("user_id"), name=data["name"], age=data.get("age"))
        db.session.add(new_individual)
        try:
            db.session.commit()
            return jsonify({'message': 'Profile successfully created'}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Profile with the name already exists'}), 400
    
    return jsonify({"message": "Wrong name syntax"}), 400
        
# To get details of all the persons in the database
@app.route('/api', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    result = []
    for person in persons:
        person_data = {"name": person.name, "age": person.age, "user_id": person.id}
        result.append(person_data)
    return jsonify(result)


# To get the person by name within the database
@app.route('/api/<name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        return jsonify({"name": person.name, "age": person.age, "user_id":person.id})
    return jsonify({'message': 'Individual not found'}), 404




@app.route('/api/<name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    if 'name' in data and is_a_valid_name(data['name']):
        person = Person.query.filter_by(name=name).first()
        if person:
            person.age = data.get('age')
            db.session.commit()
            return jsonify({'message': 'Individual updated successfully'})
        return jsonify({'message': 'Individual not found'}), 404
    return jsonify({'message': 'Invalid name provided'}), 400

@app.route('/api/<name>', methods=['DELETE'])
def delete_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Individual deleted successfully'})
    return jsonify({'message': 'Individual not found'}), 404



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

