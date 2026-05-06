from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    # 1. Collect form data
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    
    # Calculate the total count of fruits
    total_count = strawberry + raspberry + apple
    full_name = f"{first_name} {last_name}"
    
    # 2. Add the required print statement to the terminal
    print(f"Charging {full_name} for {total_count} fruits.")
        
    # 3. Get the current date and time
    current_time = datetime.datetime.now().strftime("%B %dnd %Y %I:%M:%S %p")
    
    # 4. Pass the data to the template
    return render_template(
        "checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        apple=apple,
        first_name=first_name,
        last_name=last_name,
        student_id=student_id,
        total_count=total_count,
        current_time=current_time
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)