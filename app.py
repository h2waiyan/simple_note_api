from bson.json_util import dumps
from database import Database
from models.note import Note
from database import Database
from flask import Flask, jsonify

app = Flask(__name__)

Database.initialize()

note = Note(1, "MyFirstNote", "Hello World")
note.save_to_mongo()

@app.route('/')
def Home():
    return "Hello World!"

@app.route('/notes/')
def get_stores():
    result = note.from_mongo(1)
    return dumps(result)

app.run(debug=True)