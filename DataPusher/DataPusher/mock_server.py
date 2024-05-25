from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST', 'GET', 'PUT'])
def api():
    headers = dict(request.headers)
    data = request.get_json()
    print(data)
    return jsonify({"headers": headers, "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8081)