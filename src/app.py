from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def version():
    return jsonify({"version": "v1.0.0"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0")