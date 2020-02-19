from flask import Flask, jsonify
from numeros import numero

app = Flask(__name__)

@app.route('/<int:entrada>', methods=['GET'])
def response(entrada):
    resultado = numero(entrada)
    return jsonify(resultado=resultado)

if __name__ == '__main__':
    app.run(port=5050, debug=True)