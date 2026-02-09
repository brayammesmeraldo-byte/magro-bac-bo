from flask import Flask, jsonify, request, session, redirect
import data

app = Flask(__name__)
app.secret_key = "MAGROBACBOGOLD"

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/")
def home():
    if not session.get("logged_in"):
        return redirect("/login")
    return app.send_static_file("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        if user == USERNAME and pwd == PASSWORD:
            session["logged_in"] = True
            return redirect("/")
        else:
            return "Login inválido"
    return app.send_static_file("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/api/add", methods=["POST"])
def add():
    result = request.json.get("result")
    if result in ["P", "B", "T"]:
        data.add_result(result)
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

@app.route("/api/stats")
def stats():
    return jsonify(data.get_stats())

@app.route("/api/streaks")
def streaks():
    return jsonify(data.get_streaks())

@app.route("/api/suggest")
def suggest():
    return jsonify({"suggestion": data.suggest()})

@app.route("/api/history")
def history():
    return jsonify(data.history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)