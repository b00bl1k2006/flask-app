from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['POST'])
def test_connection():
    data = request.json
    return jsonify({
        "message": "Сервер на Render работает!",
        "received_data": data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
