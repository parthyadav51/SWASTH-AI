from flask import Flask, render_template, request, redirect, url_for, session,flash
import mysql.connector
import uuid
import secrets
from flask_mail import Mail, Message

app = Flask(__name__)

def generate_secret_key():
    return secrets.token_hex(16)  

app.secret_key = generate_secret_key() 


db = mysql.connector.connect(
    host='Parths-MacBook-Air.local',
    user='root',
    password='Notlove@123',
    database='login')

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            api_key = str(uuid.uuid4())
            session['api_key'] = api_key
            return redirect(url_for('login_success', api_key=api_key))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

@app.route('/swasthaai2')
def login_success():
    api_key = request.args.get('api_key')
    if 'api_key' in session and session['api_key'] == api_key:
        return render_template('swasthaai2.html')
    else:
        flash('Unauthorized access', 'error')
    return redirect(url_for('loginfail.html'))
@app.route('/forget')
def forget():
    return render_template('forgetpage.html')
@app.route('/ayurveda')
def ayurveda():
    return render_template('ayurveda.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/support1')
def support():
    return render_template('support.html')
@app.route('/const')
def const():
    return render_template('const.html')
@app.route('/disease/disease1')
def dis1():
    return render_template('/disease/disease1.html')
@app.route('/disease/medicine13')
def med13():
    return render_template('/disease/medicine13.html')
@app.route('/disease/medicine2')
def med2():
    return render_template('/disease/medicine2.html')
@app.route('/disease/medicine4')
def med4():
    return render_template('/disease/medicine4.html')
@app.route('/disease/medicine10')
def med10():
    return render_template('/disease/medicine10.html')
@app.route('/disease/medicine6')
def med6():
    return render_template('/disease/medicine6.html')
@app.route('/disease/medicine11')
def med11():
    return render_template('/disease/medicine11.html')
@app.route('/disease/medicine5')
def med5():
    return render_template('/disease/medicine5.html')
@app.route('/disease/medicine3')
def med3():
    return render_template('/disease/medicine3.html')
@app.route('/disease/medicine7')
def med7():
    return render_template('/disease/medicine7.html')
@app.route('/disease/medicine14')
def med14():
    return render_template('/disease/medicine14.html')

@app.route('/disease/medicine16')
def med16():
    return render_template('/disease/medicine16.html')
@app.route('/disease/medicine8')
def med8():
    return render_template('/disease/medicine8.html')
@app.route('/disease/medicine12')
def med12():
    return render_template('/disease/medicine12.html')
@app.route('/disease/medicine9')
def med9():
    return render_template('/disease/medicine9.html')
@app.route('/disease/medicine15')
def med15():
    return render_template('/disease/medicine15.html')


if __name__ == '__main__':
    app.run(debug=True)
