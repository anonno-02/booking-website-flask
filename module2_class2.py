from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Displaying a normal text in a webpage:

# @app.route('/<name>/')    # This is very important. This is the url rule, the name which is to be added at the end of the url given by the terminal. Use slashes at both start and end, otherwise will show error in some cases.

# def hello_world(name):
#     return "Welcome to the Flask project, %s." %name

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Creating conditional access:

# @app.route('/admin/')

# def hello_admin():
#     return "Hello unconditional admin"

# @app.route('/guest/<guest>/')

# def hello_guest(guest):
#     return "Hello unconditional guest, %s!" %guest

# @app.route('/user/<user>/')

# def hello_user(user):
#     if user == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest = user))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# Combining backend with frontend:

@app.route('/success/<successname>/')

def success(successname):
    return "Welcome %s!" %successname

@app.route('/login/', methods = ['POST', 'GET'])

def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', successname = user))

if __name__ == '__main__':
    app.run(debug = True)