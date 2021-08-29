from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = add(a, b)
    return f'{sum}'

@app.route('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    diff = sub(a, b)
    return f'{diff}'

@app.route('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    times = mult(a, b)
    return f'{times}'

@app.route('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    try:
        divided = div(a, b)
    except:
        divided = "cannot divide by 0"
    return f'{divided}'

@app.route('/math/<operation>')
def all_in_one(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    if operation == 'add':
        total = add(a, b)
    elif operation == 'sub':
        total = sub(a, b)
    elif operation == 'mult':
        total = mult(a, b)
    elif operation == 'div':
        total = div(a, b)
    else:
        return 'not a valid operation'
    return f'{total}'