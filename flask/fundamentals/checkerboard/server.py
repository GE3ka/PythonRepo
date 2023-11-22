from flask import Flask  , render_template 
app = Flask(__name__)  

@app.route('/checkerboard/<int:x>/<int:y>/<string:color1>/<string:color2>')
def play(x,y,color1,color2):         
    return  render_template("index.html",rows=x,columns=y,color_1=color1,color_2=color2)

if __name__=="__main__":   
    app.run(debug=True)    