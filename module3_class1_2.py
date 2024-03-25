from flask import Flask, redirect, render_template

app = Flask(__name__)

# Getting and understanding an error:

@app.route('/error_500')
def error_500():
    x = 1/0
    return "This won't run!"

if __name__ == '__main__':
    app.run(debug = True)