from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "booking.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bookings (name, email, date, slot) VALUES (?, ?, ?, ?)",
        (
            request.form['name'],
            request.form['email'],
            request.form['date'],
            request.form['slot']
        )
    )
    conn.commit()
    conn.close()
    return redirect('/bookings')

@app.route('/bookings')
def bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    data = cursor.fetchall()
    conn.close()
    return render_template('bookings.html', bookings=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
