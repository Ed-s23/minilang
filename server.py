# server.py
from flask import Flask, request, jsonify, send_from_directory
from interpreter import EvalVisitor, evaluate_source
import io
import contextlib

app = Flask(__name__, static_url_path="", static_folder="web")

@app.route("/")
def index():

    return send_from_directory("web", "index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    print(" Código recibido:", data)
    source = data.get("code", "")
    visitor = EvalVisitor()

    try:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            evaluate_source(source + "\n", visitor)
        result = output.getvalue()
        print("Resultado:", result)
        return jsonify({"output": result, "error": None})
    except Exception as e:
        print(" Error:", e)
        return jsonify({"output": "", "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
