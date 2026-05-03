from flask import Flask, render_template

app = Flask(__name__)

# Route for Level 1: When user visits /play
@app.route('/play')
def index():
    # Renders the template with default values: 3 boxes and the color 'blue'
    return render_template('index.html', times=3, color='blue') # Note: Fixed the variable name to match the template (times instead of time)

# Route for Level 2: When user visits /play/<x>
@app.route('/play/<x>')
def level_two(x):
    # Converts the string 'x' from the URL to an integer, keeping the color 'blue'
    return render_template('index.html', times=int(x), color='blue')

# Route for Level 3: When user visits /play/<x>/<color>
@app.route('/play/<x>/<color>')
def level_three(x, color):
    # Converts the string 'x' to an integer and passes the custom color from the URL
    return render_template('index.html', times=int(x), color=color)

if __name__ == "__main__":
    # Runs the Flask application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)