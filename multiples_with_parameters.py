
from flask import Flask


# multiple routes
app = Flask(__name__)

@app.route('/')
def home():
    return "This is the HomePage"

@app.route('/about')
def about():
    return "This is the About Page"

@app.route('/contact')
def contact():
    return "This is the Contact Page"


# using route parameters


@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name.capitalize()}!"


@app.route('/number/<int:number>')
def square(number):
    return f"Square of {number} is {number**2}"



if __name__ == '__main__':
    app.run(debug= True)
    
   