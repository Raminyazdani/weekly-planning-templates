from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.post("/entry")
def receive_entry():
    data = request.get_json(force=True)  # JSON from the browser
    # ---- Run your Python logic here ----
    # Example 1: call a function
    # result = do_something(data)

    # Example 2: call an external Python script with JSON via stdin
    # proc = subprocess.run(
    #     ["python", "my_script.py"],
    #     input=json.dumps(data).encode("utf-8"),
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     check=False
    # )
    # result_text = proc.stdout.decode("utf-8")

    # For demo: just echo back
    return jsonify({"ok": True, "received": data})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
