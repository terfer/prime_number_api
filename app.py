"""Flask module for the API"""
from importlib.resources import path
from flask import Flask, request, abort

app = Flask(__name__)

path = 'data/list.data'

try:
    open(path, 'r').readlines()[-1]
except OSError:
    data_file = open(path, 'w', encoding="utf-8")
    data_file.write("1")
    data_file.close()


def is_prime(num: int):
    """Function to calculate num prime numbers"""
    for i in range(2, int(num/2)+1):
        if ((num % i) == 0) & (num != i):
            return False
    return True


@app.route('/queue', methods=['POST'])
def calculate_num_prime():
    """API method to set how many prime numbers have to calculate"""
    if not request.json or not 'num_calc' in request.json:
        abort(400)
    with open(path, 'r', encoding="utf-8") as data_file:
        first_number_calculated, data_new = int(
            data_file.readlines()[-1]), len(data_file.read())
    number_calculations = int(request.json['num_calc']) + data_new
    first_number_calculated += 1
    with open(path, 'a', encoding="utf-8") as data_file:
        while data_new < number_calculations:
            if is_prime(first_number_calculated):
                data_file.write("\n")
                data_file.write(str(first_number_calculated))
                data_new += 1
            first_number_calculated += 1
    return "Success"


@app.route('/get_primes', methods=['GET'])
def get_prime_numbers():
    """API method to get all prime numbers calculated before"""
    with open(path, 'r', encoding="utf-8") as data_file:
        data = str(data_file.read())
    return data


app.run(host='localhost', port=20044, debug=False)
