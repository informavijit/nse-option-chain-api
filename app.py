from flask import Flask, jsonify, request
from nsepython import option_chain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/nse/option-chain")
def get_option_chain():
    symbol = request.args.get("symbol", "NIFTY")
    try:
        data = option_chain(symbol)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ NSE Option Chain Microservice is running!"

if __name__ == "__main__":
    app.run(debug=True)
