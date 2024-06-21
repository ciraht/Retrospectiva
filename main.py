from flask import Flask, render_template, request, redirect, url_for

import subprocess


app = Flask(__name__)
contador_cliques = 0

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/local1')
def local1():
    return render_template('local1.html')
@app.route('/local2')
def local2():
    return render_template('local2.html')
@app.route('/local3')
def local3():
    return render_template('local3.html')
@app.route('/local4')
def local4():
    return render_template('local4.html')
@app.route('/local5')
def local5():
    return render_template('local5.html')
@app.route('/local6')
def local6():
    return render_template('local6.html')
@app.route('/local7')
def local7():
    return render_template('local7.html')
@app.route('/local_secreto')
def local_secreto():
    return render_template('local_secreto.html',     contador=contador_cliques)






@app.route('/incrementar', methods=['POST'])
def incrementar():
    global contador_cliques
    contador_cliques += 1

    numero_aleatorio = 5  # Exemplo: redirecionar quando o contador atingir 5

    if contador_cliques == numero_aleatorio:
        return redirect(url_for('outra_pagina'))

    return redirect(url_for('local_secreto'))


@app.route('/outra_pagina')
def outra_pagina():
    return render_template('outra_pagina.html')


if __name__ == '__main__':
    app.run(debug=True)