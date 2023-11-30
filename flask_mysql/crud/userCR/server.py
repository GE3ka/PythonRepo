from flask import Flask,render_template,request,redirect
from user import User

app = Flask(__name__)
app.secret_key = "123456"

@app.route('/')
def display():
    users=User.display_all()
    return render_template('/display.html',users_list=users)

@app.route('/add')
def display_create():
    return render_template('/create.html')

@app.route('/create',methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.create(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)