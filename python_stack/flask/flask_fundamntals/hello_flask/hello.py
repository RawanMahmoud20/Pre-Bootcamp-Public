from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def hello_world():
    return "Hello world!"

# Trainees Page (HTML)
@app.route("/trainees")
def trainees():
    return render_template("index.html")

# Dynamic Route (Profile Page)
@app.route("/trainees/<id>")
def trainees_profile(id):
    return f"{id}'s profile"

# Run Server
if __name__ == "__main__":
    app.run(debug=True)