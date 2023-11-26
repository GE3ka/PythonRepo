from flask import Flask,session,redirect,render_template,request

app=Flask(__name__)
app.secret_key="abcd"
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process():
    data = request.form
    session['name']=data['name']
    session['location']=data['location']
    session['language']=data['language']
    session['comment']=data['comment']
    return render_template('process.html',name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])    
if __name__==('__main__'):
    app.run(debug=True)