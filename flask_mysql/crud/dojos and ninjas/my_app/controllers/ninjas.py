from my_app import app
from flask import Flask, render_template ,request,redirect
from my_app.models.dojo import Dojo
from my_app.models.ninja import Ninja

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.display_dojos()
    return render_template('/ninja.html',dojos=dojos)


@app.route('/add_ninja/create',methods=["post"])
def create_ninja():
    data=request.form
    Ninja.add_dojo(data)
    return redirect('/')




