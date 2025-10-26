from flask import Flask, send_file, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return send_file("treino_ppl_player_standalone.html")

if __name__ == "__main__":
    # Run the app on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
