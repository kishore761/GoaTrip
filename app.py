from flask import Flask, render_template, request, redirect

app = Flask(__name__)

registrations = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    phone = request.form["phone"]
    place = request.form["place"]

    registrations.append({
        "name": name,
        "phone": phone,
        "place": place
    })

    return """
    <h2>Registration Successful ✅</h2>
    <a href="/">Go Back</a>
    """

@app.route("/admin")
def admin():
    return render_template("admin.html", registrations=registrations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)
