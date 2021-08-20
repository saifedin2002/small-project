"""
create flask app
"""
from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html',title= 'CALC APP')
@app.route('/contact',methods = ['GET', 'POST'])
def sum_number():
    result = None 
    if request.method == 'POST' :
        n1 = request.form['num1']
        op = request.form['op']
        n2 = request.form['num2']
        try:
            result = eval(f"{n1}{op}{n2}")
        except BaseException as error:
            result = f"result = '{error}' "
    return render_template('contact.html',title= 'CALC APP',result=result)    


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)


 
  
 