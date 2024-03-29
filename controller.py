from flask import Flask, request, make_response
import json
from logic import recommend
app = Flask(__name__)

@app.route('/similarity-alg/health')
def hello_world():
    return 'Hi there, im healthy!'


@app.route('/api/v2/similarity-alg/flow/recommend', methods=['POST'])
def reccommend():
    person = request.json
    return json.dumps(recommend(person['name'], person['data'], 5)), 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)