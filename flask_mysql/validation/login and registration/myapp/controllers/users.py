from myapp import app
from flask import Flask, render_template ,request,redirect,session
from myapp.models.user import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    print(User.validation(data))
    result=User.validation(data)
    if result:
        User.create(data)
    return redirect('/')

@app.route('/login',methods=['POST'])
def login():
    data=request.form
    user_found=User.getuser_by_email(data)
    if User.login_validation(data):
        session['id']=user_found.id
        session['first_name']=user_found.first_name
        session['last_name']=user_found.last_name
        return render_template('dashboard.html')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





