from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from pymongo import MongoClient


app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def list():
    mongo_uri = "mongodb://mongos:27017"

    client = MongoClient(mongo_uri)
    db = client.notes
    collection = db.notes

    cursor = collection.find()

    notes = []

    for note in cursor:
        # Se adicionó para poder manejar ObjectID
        note['_id'] = str(note['_id'])
        notes.append(note)

    return notes

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
