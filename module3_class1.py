from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)

## Creating a booking application with database:

@app.route('/')

def success():
    return render_template('hello2.html')

@app.route('/booking2')

def booking():
    return render_template('booking2.html')

@app.route('/bookinglist')

def bookinglist():
    all_bookings = Booking.query.all()
    return render_template('bookinglist.html', bookings=all_bookings)


@app.route('/booked2', methods = ['POST'])

def booked():
    booker = request.form.get('name')
    booked_service = request.form.get('service')

    booking = Booking(name=booker, service=booked_service)
    db.session.add(booking)
    db.session.commit()
    return redirect(url_for('bookinglist'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)