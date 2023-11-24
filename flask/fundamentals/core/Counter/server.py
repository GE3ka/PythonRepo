from flask import Flask, render_template, session,redirect
app = Flask(__name__)
app.secret_key = 'this is a key'

@app.route('/')

def home():
    if 'times' not in session:
        session['times']=0
    session['times'] += 1    
    
    return render_template('index.html',count=session['times'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ ==('__main__'):
    app.run(debug=True)
