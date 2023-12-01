from my_app import app
from flask import Flask, render_template ,request,redirect
from my_app.models.dojo import Dojo
@app.route('/')
def home():
    dojos=Dojo.display_dojos()

    return render_template('home.html',dojos=dojos)

@app.route('/add_dojo',methods=["post"])
def add_dojo():
    data=request.form
    Dojo.add_dojo(data)
    return redirect('/')

@app.route('/show/<int:id>')
def show_dojo(id):
    data={"id":id}
    ninjas=Dojo.show_dojo(data)
    return render_template('/display.html',ninjas=ninjas)