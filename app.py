from flask import Flask, request, abort
from json import load

app = Flask(__name__)

try:
    open(f'data/list.data', 'r').readlines()[-1]
except:
    db = open('data/list.data', 'w')
    db.write("1")
    db.close()

def esPrimo(num: int):
    for i in range(2, int(num/2)+1):
        if ((num % i) == 0)  & (num != i):
            return False
    return True

@app.route('/queue', methods=['POST'])
def calculate_num_prime():
    first_number_calculated = int(open(f'data/list.data', 'r').readlines()[-1])
    data_new = len(open(f'data/list.data', 'r').read())
    db = open(f'data/list.data', 'a')
    first_number_calculated += 1
    if not request.json or not 'num_calc' in request.json:
        abort(400)
    number_calculations = int(request.json['num_calc']) + data_new
    while data_new < number_calculations:
        if esPrimo(first_number_calculated):
            db.write("\n")
            db.write(str(first_number_calculated))
            data_new += 1
        first_number_calculated += 1
    db.close()
    return "Success"

@app.route('/get_primes', methods=['GET'])
def get_prime_numbers():
    db = load(open(f'data/list.data', 'r'))
    data = db.read()
    db.close()
    return data

app.run(host='localhost', port=20044, debug=False)