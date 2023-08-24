from flask import Flask, request

app = Flask(__name__)

"""FIRST:
   send an integer in the URL, get the integer squared back"""
@app.route('/squared/<int:number>', methods=['GET'])
def get_value(number):
    result = number ** 2
    return {'squared': result}

"""SECOND:
   send a GET request, always get the same value back"""
@app.route('/static', methods=['GET'])
def get_static_value():
    return ["this","is","always","returned"]

"""THIRD:
   POST the 'answer to life, the universe, and everything' as '42' and get 'Correct!' else, get 'Wrong!'"""
@app.route('/answer', methods=['POST'])
def check_value():
    # takes the json attached to incoming request
    data = request.json
    correct_value = "42"
    
    answer= data.get("value")

    if answer == "42":
        return "Correct!"
    else:
        return "Wrong!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2225)

