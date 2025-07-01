from flask import Flask,render_template

app = Flask (__name__)

@app.route('/')
def hello():
   return 'Hello Flask'
@app.route('/sub1')
def sub1(): 
   return 'SUB1 Page'
if __name__ == '__main__':
    app.run(debug = True, port = 80, host = '0.0.0.0')

#chay file = cd Session 12 -> sudo python3 flaskweb.py