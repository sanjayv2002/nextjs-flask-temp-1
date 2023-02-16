from flask import Flask , jsonify
from flask_cors import cross_origin 
import os

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return jsonify({"member":"Member1"})



if __name__ == '__main__':
    app.run(debug = True, port = os.getenv("PORT", default = 5000))

