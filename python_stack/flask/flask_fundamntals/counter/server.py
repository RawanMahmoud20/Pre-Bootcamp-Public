from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = "abc123"

@app.route('/')
def index():
    if 'count' not in session: 
        session['count'] = 0   
    else:       
      session['count'] += 1       
    return render_template('index.html', count=session['count'])


@app.route('/destroy_session')
def destroy_session():
    session.clear()   
    return redirect('/')  

if __name__ == "__main__":
    app.run(debug=True)