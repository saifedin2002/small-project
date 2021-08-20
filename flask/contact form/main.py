"""
flask app
whit contact fom
"""
from include.contact_form import contact_from
from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',title= "flask")
@app.route('/contact',methods = ['POST','GET'])
def contact():
    contact_from()  
        

    return render_template('contact.html',title= "flask" )    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 