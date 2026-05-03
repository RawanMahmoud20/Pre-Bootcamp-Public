from flask import Flask

app = Flask(__name__)

# Root route - responds with "Hello World!"
@app.route('/')
def index():
    return 'Hello World!'

# Champion route - responds with "Champion!"
@app.route('/champion')
def champion():
    return 'Champion!'

# Say route - takes a variable name and returns a personalized greeting
@app.route('/say/<name>')
def say_hello(name):
    return f"Hi {name}!"

# Repeat route - repeats the given word based on the number specified
# <int:num> ensures the URL parameter is an integer (Ninja Bonus)
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    # Multiply the string by the number to repeat it
    return (word + " ") * num

# Error handler - catches invalid routes and responds with an error message (Sensei Bonus)
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)