# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Route to handle form submission (POST request only)





@app.route('/result', methods=['POST'])
def result():
    # Print form data in terminal (for debugging purposes)
    print(request.form)

    # Get form data using the name attribute from the form
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    gender = request.form['gender']  # Added gender field
    comment = request.form['comment']

    # Render result.html and pass the collected data
    return render_template(
        'result.html',
        name=name,
        location=location,
        language=language,
        gender=gender,
        comment=comment
    )

# Run the application in debug mode on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)