from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, UserMixin, current_user, login_required, login_user, logout_user)
from flask_principal import Permission, Principal, RoleNeed

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
principal = Principal(app)

## Create authorization and authentication system:

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('success'))
        else:
            return "Invalid username or password!"
    return(render_template('login.html'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))   

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists, try again please!"
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')



## Creating a booking application with database:

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)

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