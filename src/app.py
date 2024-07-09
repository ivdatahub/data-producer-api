from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json(force=True)
        data_str = json.dumps(data)
        message = data_str.encode('utf-8')
        return jsonify({
            "status": "success",
            "total_lines_received": len(data)
        }), 200
    except Exception as e:
        return jsonify({"status": "error",
                        "message": "Bad Request",
                        "exception": e
                        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
