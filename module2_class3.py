from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

## Creating a booking application;

@app.route('/')

def success():
    return render_template('hello.html')

@app.route('/booking')

def booking():
    return render_template('booking.html')


@app.route('/booked', methods = ['POST'])

def booked():
    booker = request.form.get('name')
    booked_service = request.form.get('service')
    return f"Thank you {booker}, for booking the {booked_service} service!"

if __name__ == '__main__':
    app.run(debug = True)