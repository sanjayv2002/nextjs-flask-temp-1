from flask import Flask , jsonify
from flask_cors import cross_origin 
import os

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return jsonify({message:"TEMPLATE READY"})


#"message":"This is the flask template you can work on",["purpose":"This template can be used as server backend which send the JSON responces to the frontend"
if __name__ == '__main__':
    app.run(debug = True, port = os.getenv("PORT", default = 5000))

