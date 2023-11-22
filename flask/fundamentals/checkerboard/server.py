from flask import Flask  , render_template 
app = Flask(__name__)  

@app.route('/checkerboard/<int:x>/<int:y>')
def play(x,y):         
    return  render_template("index.html",rows=x,columns=y)

if __name__=="__main__":   
    app.run(debug=True)    