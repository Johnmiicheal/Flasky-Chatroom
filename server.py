from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    data = {
        "cats": 5,
        "people": 10,
        "dogs": 4
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)