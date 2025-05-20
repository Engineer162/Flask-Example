# pip install libraries
from flask import Flask, render_template, request, redirect
from app.config import Config
from app.forms import Q1_Form, Q2_Form, Q3_Form, Q4_Form
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
            cursor.execute('INSERT INTO Spørgsmål1(result) VALUES ('+valg+')')
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


@app.route('/q4/', methods=['POST', 'GET'])
def q4():
    q4_form = Q4_Form()
    if q4_form.validate_on_submit():
        if q4_form.checkbox.data:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            checkbox = q4_form.checkbox.data
            print(checkbox)
            cursor.execute('INSERT INTO Spørgsmål2(result) VALUES (?)', (checkbox,))
            conn.commit()
            conn.close()

            return redirect('/')
    return render_template('q4.html', q4_form = q4_form)

if __name__ == '__main__':
    app.debug = True
    #app.run(debug=True) #Koer kun paa localhost
    app.run(host='0.0.0.0', port=8080)
