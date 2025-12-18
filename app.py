from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='RDS-ENDPOINT',
    user='admin',
    password='password',
    database='bookingdb'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    slot = request.form['slot']

    with connection.cursor() as cursor:
        sql = "INSERT INTO bookings (name, email, date, slot) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, email, date, slot))
        connection.commit()

    return redirect('/bookings')

@app.route('/bookings')
def bookings():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM bookings")
        data = cursor.fetchall()
    return render_template('bookings.html', bookings=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
