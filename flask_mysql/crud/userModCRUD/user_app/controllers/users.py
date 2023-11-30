from user_app import app
from flask import render_template, redirect, request
from user_app.models.user import User



@app.route('/')
def display():
    users=User.display_all()
    return render_template('/main.html',users_list=users)

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

@app.route('/show_one_user/<int:id>')
def one_user_details(id):
    one_user = User.display_one(id)
    return render_template('show_one_user.html',one_user=one_user)
    
@app.route('/update/<int:id>')
def update_user(id):
    user_to_update=User.display_one(id)
    return render_template('update.html',user_to_update=user_to_update)

@app.route('/update/<int:id>/edit_mode',methods=['POST'])
def  edit_user(id):
    data = {
    "id": id,    
    "first_name": request.form["first_name"],
    "last_name" : request.form["last_name"],
    "email" : request.form["email"]
    }   
    User.update_user(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    data={"id":id}
    User.delete_user(data)
    return redirect('/')
