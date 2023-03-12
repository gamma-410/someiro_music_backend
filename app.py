from flask import Flask, request, jsonify
from flask_cors import CORS
from json_serializable import JSONSerializable  # SpecialThanks...!
from note import Note, NoteDetail

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)
JSONSerializable(app)


@app.route('/')
def index():
    data = Note("_someiro_")
    return jsonify(data)

@app.route('/<string:id>')
def detail(id):
    data = NoteDetail(id)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)