from flask import Flask, request, render_template
import pymysql

db = None
cur = None

app = Flask(__name__)

def select(query):
    global db
    db = pymysql.connect(
        host='192.168.1.10',
        user='root',
        password='1234',
        db='mysql',
        charset='utf8'
    )
    cur = db.cursor()
    cur.execute(query)
    result = cur.fetchall()
    db.close()
    return result

@app.route('/chart') # them chart vao sau link
def lm35_chart():
    sql = "SELECT DATATIME, TEMP FROM temperature ORDER BY DATATIME ASC LIMIT 100"
    result = select(sql)
    return render_template("chart.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
