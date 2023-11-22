from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!"

@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<string:username>')
def hello_user(username):
    return f"Hi {username} !"

@app.route('/repeat/<int:num>/<string:keyword>')
def repeat(num,keyword):
    phrase = ""
    if type(num) == int:
        for i in range(num):
            phrase += keyword + "</br> "
            
        return phrase
    else:
        return "Sorry! No response. Try again. "
if __name__=="__main__":   
    app.run(debug=True)       