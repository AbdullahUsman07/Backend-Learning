
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask! This is my First Backend app"

if __name__ == '__main__':
    app.run(debug = True)



    
