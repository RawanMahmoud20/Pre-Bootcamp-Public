from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# 1. Home route - returns a simple greeting
# URL: localhost:5000/
@app.route('/')
def hello_world():
    return "Hello World!"


# 2. Champion route - returns "Champion!"
# URL: localhost:5000/Champion
@app.route('/Champion')
def champion():
    return "Champion!"


# 3. Dynamic route using a path variable
# URL: localhost:5000/say/<name>
# Capitalizes the first letter of the name using .capitalize()
@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name.capitalize()}!"


# 4. Repeat route - repeats a word a given number of times
# URL: localhost:5000/repeat/<num>/<word>
# <int:num> ensures the first variable is treated as an integer
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return f"{word} " * num


# SENSEI BONUS: Custom 404 error handler
# Catches any request to a route that doesn't exist
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404


# Run the app in debug mode when executed directly
# Debug mode auto-reloads on code changes and shows detailed errors
if __name__ == "__main__":
    app.run(debug=True)