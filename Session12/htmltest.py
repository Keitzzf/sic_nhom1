from flask import Flask,render_template

app = Flask (__name__)

@app.route('/')
def index():
   return render_template('test.html')

if __name__ == '__main__':
    app.run(debug = True, port = 80, host = '0.0.0.0')

#chay file = cd Session12 -> sudo python3 htmltest.py