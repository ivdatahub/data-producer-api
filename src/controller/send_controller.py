import json
from flask import jsonify


def send(data):
    try:
        data_str = json.dumps(data)
        message = data_str.encode('utf-8')

        if len(data) > 1:
            return jsonify({
                "status": "success",
                "total_lines_received": len(data),
            }), 200
        else:
            return jsonify({
                "status": "success",
                "received_data": data,
            }), 200

    except Exception as e:
        return jsonify({"status": "error",
                        "message": "Bad Request",
                        "exception": e
                        }), 400
