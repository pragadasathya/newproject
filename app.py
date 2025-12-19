from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
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
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = "INSERT INTO bookings (name, email, date, slot) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (
            request.form['name'],
            request.form['email'],
            request.form['date'],
            request.form['slot']
        ))
        conn.commit()
    conn.close()
    return redirect('/bookings')

@app.route('/bookings')
def bookings():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bookings")
        data = cursor.fetchall()
    conn.close()
    return render_template('bookings.html', bookings=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
