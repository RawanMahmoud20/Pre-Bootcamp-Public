from flask import Flask, session, render_template, request, redirect
import random

# Create Flask application
app = Flask(__name__)

# Secret key is required for session management
app.secret_key = "abc123"


# Home route - initializes game state
@app.route('/')
def index():
    # If this is the first visit, initialize gold and activities
    if 'gold' not in session:
        session['gold'] = 0  # Player starts with 0 gold
        session['activities'] = []  # Empty activity log
    
    # Render main page with current gold and activity log
    return render_template('main.html', 
                           gold=session['gold'],
                           activities=session['activities'])


# Route to process building selection
@app.route('/process_money', methods=['POST'])
def process_money():
    
    # Get selected building from form
    building = request.form['building']
    
    # Determine gold earned based on building type
    if building == 'farm':
        earned = random.randint(10, 20)
        message = f"Earned {earned} golds from the farm!"
        color = "green"
        
    elif building == 'cave':
        earned = random.randint(5, 10)
        message = f"Earned {earned} golds from the cave!"
        color = "green"
        
    elif building == 'house':
        earned = random.randint(2, 5)
        message = f"Earned {earned} golds from the house!"
        color = "green"
        
    elif building == 'casino':
        earned = random.randint(-50, 50)  # Can win or lose
        
        if earned >= 0:
            message = f"Earned {earned} golds from the casino!"
            color = "green"
        else:
            message = f"Lost {abs(earned)} golds at the casino... Ouch!"
            color = "red"

    # Update total gold
    session['gold'] += earned

    # Add activity to log
    session['activities'].append({
        'message': message,
        'color': color
    })

    # Mark session as modified (important when modifying mutable objects)
    session.modified = True
    
    # Redirect back to home page
    return redirect('/')


# Reset game route
@app.route('/reset')
def reset():
    session.clear()  # Clear all session data
    return redirect('/')


# Run application
if __name__ == "__main__":
    app.run(debug=True)