# pip install Flask
from flask import Flask, render_template, request, redirect
from app.config import Config
from app.forms import Q1_Form, Q2_Form, Q3_Form
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
db = 'database.db'

@app.route('/')
def home():
    # Her kan fx hentes data og sættes ind i html-koden
    txt = "Jinja and Flask"
    return render_template('index.html', title=txt)

@app.route('/q1/', methods=['POST', 'GET'])
def q1():
    q1_form = Q1_Form()
    if q1_form.validate_on_submit():
        if q1_form.valg.data:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            valg = q1_form.valg.data
            print(valg)
            cursor.execute('INSERT INTO driver(result) VALUES ('+valg+')')
            conn.commit()
            conn.close()
            """
            Ekstra-opgave:
            En måde at sikre sig at brugeren ikke kan stemme to
            gange, er ved at sætte en cookie her v.hj.a.javascript.
            https://www.w3schools.com/js/js_cookies.asp

            """
            return redirect('/')
    return render_template('q1.html', q1_form = q1_form)

@app.route('/q2/', methods=['POST', 'GET'])
def q2():
    q2_form = Q2_Form()
    if q2_form.validate_on_submit():
        if q2_form.pizza:
            pizza = q2_form.pizza.data
            print(pizza)
            print("Din IP adresse er: "+request.remote_addr)
            # Her sætter vi data ind i en tabel
            return redirect('/')
    return render_template('q2.html', q2_form = q2_form)

@app.route('/q3/', methods=['POST', 'GET'])
def q3():
    q3_form = Q3_Form()
    if q3_form.validate_on_submit():
        if request.form.get("svar1") != None:
            brugersvar = 1 #STX
        if request.form.get("svar2") != None:
            brugersvar = 2 #HHX
        if request.form.get("svar3") != None:
            brugersvar = 3 #HTX
        print(brugersvar)
        return redirect('/')
    return render_template('q3.html', q3_form = q3_form)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=8080)
