from flask import Flask, render_template

app = Flask(__name__)


# Basic route: renders an 8x8 checkerboard with red and black
@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color_one='red', color_two='black')


# Single variable route: custom number of rows, 8 columns by default
# /<int:x> to ensure the number passing in integer 
@app.route('/<int:x>')
def row_only(x):
    return render_template("index.html", row=x, col=8, color_one='red', color_two='black')


# Ninja Bonus: two variables for custom rows and columns
@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template("index.html", row=x, col=y, color_one='red', color_two='black')


# Sensei Bonus: full customization — rows, columns, and both colors
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def custom_board(x, y, color1, color2):
    return render_template("index.html", row=x, col=y, color_one=color1, color_two=color2)


# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)