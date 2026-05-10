# Import required libraries
from flask import Flask, session, render_template, request, redirect
import random

# Create Flask application instance
app = Flask(__name__)

# Secret key is required to use sessions
app.secret_key = "abc123"

# Route for the home page
@app.route('/')
def index():
    # If there is no number stored in session, generate one
    if 'number' not in session:
        session['number'] = random.randint(1, 100)  # Generate random number between 1 and 100
        session['attempts'] = 0  # Initialize number of attempts
    
    # Render the main page
    return render_template('index.html')


# Route to handle user's guess (POST request)
# this is recived dara from form 
@app.route('/guess', methods=['POST'])
def guess():
    # Get user input from the form and convert it to integer
    user_guess = int(request.form['guess'])
    
    # Retrieve the secret number from session
    secret_number = session['number']
    
    # Increase attempts counter
    session['attempts'] += 1

    # Compare user guess with secret number
    if user_guess < secret_number:
        result = "too_low"      # Guess is smaller than secret number
    elif user_guess > secret_number:
        result = "too_high"     # Guess is greater than secret number
    else:
        result = "correct"      # Guess is correct

    # Render template with result and attempts
    return render_template('index.html', 
            result=result, 
            number=secret_number,
            attempts=session['attempts'])


# Route to reset the game
@app.route('/play_again')
def play_again():
    session.clear()  # Clear all session data (reset game)
    return redirect('/')  # Redirect to home page


# Run the application
if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development