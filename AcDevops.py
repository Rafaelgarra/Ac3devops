import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def calcula_primos():
    quantd = 100
    aculmu = " "
    cont = 0
    conti = quantd
    zikin = 0
    i = 0
    while zikin <= quantd:
        cont = 0
        i += 1
        for c in range(1, conti):
            if i % c == 0:
                cont += 1
                conti += 1
        if cont == 2:
            aculmu = aculmu + str(i) + ", "
            zikin += 1
        cont = 0
    return aculmu



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
