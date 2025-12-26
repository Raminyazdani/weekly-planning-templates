from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/entry")
def receive_entry():
    data = request.get_json(force=True)
    # For now, just echo back
    return jsonify({"ok": True, "received": data})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
