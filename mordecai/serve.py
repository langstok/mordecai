import logging

import os
from flask import Flask, jsonify, request
from mordecai import Geoparser


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

es_hosts = os.environ.get('ES_HOSTS')
es_port = os.environ.get('ES_PORT')



app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route('/api/geoname', methods=['GET', 'POST'])
def process_geoname():
    data = {}
    if request.method == 'GET':
        if 'text' not in request.url:
                raise ValueError('You need to request param "text"')
        data['text'] = request.args.get('text')
    else:
        data = request.get_json(silent=True)
    text = str(data['text'])
    print(text)
    geo = Geoparser(es_hosts=es_hosts, es_port=es_port)
    print("geoparser loaded")
    response = geo.geoparse(text)
    print(response)
    return jsonify(str(response))


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
