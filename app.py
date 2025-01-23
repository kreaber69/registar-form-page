from flask import Flask, make_response, request, render_template, session , redirect , url_for
from cs50 import SQL
from flask_mail import Mail, Message
from random import randint
import secrets
import string
import re

app = Flask(__name__)
db = SQL("sqlite:///static/registants.db")
app.secret_key = secrets.token_hex(24)



app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'sahhara1253desert@gmail.com'
app.config['MAIL_PASSWORD'] = 'cixf xvpi dsab ffxi'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/", methods=["POST", "GET"])
def index():

    message = session.pop('message', None)
    return render_template('index.html' , message=message)

@app.route("/verify", methods=["POST", "GET"])
def verify():

    name = request.form.get("name1")
    mail = request.form.get("mail1")
    passw = request.form.get("passw1")
    existing_user = db.execute("SELECT name FROM registants WHERE name = ?", name)
    
    if existing_user:
        session['message'] = 'Name already exists'
        return redirect(url_for("index"))

        
    session["name"] = name
    session["mail"] = mail
    session["passw"] = passw

    pat1 = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    pat2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|~]).{8,}$'

    if not re.match(pat1, mail) or not re.match(pat2, passw) or not name:
        return render_template("fallure.html")
    
    otp = randint(000000, 999999)
    session['otp'] = otp
    
    man = Message(subject='OTP', sender='sahhara1253desert@gmail.com', recipients=[mail])
    man.body = str(otp)
    Mail(app).send(man)
    
    return render_template("verifiction.html")

@app.route('/validate', methods=['POST', 'GET'])
def validate():
    user_otp = request.form['otp']
    otp = session.get('otp')

    if otp is None:
        return render_template("fallure.html")
    try:
        if otp == int(user_otp):
            print("hellow world")
    except:
        session.clear()
        return render_template("fallure.html")

   
    if otp == int(user_otp):
        name2 = session["name"]
        mail =session["mail"]
        passw = session["passw"]
        secure_random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
        db.execute("INSERT INTO registants(id ,name, mail, pass) VALUES (? ,?, ?, ?)", secure_random_string , name2, mail, passw)
        id2 = db.execute("select id from registants where name = ?" , name2)
        id2 = id2[0]["id"]
        key = request.cookies.get('key', '1')
        try:
            key = int(key)
        except ValueError:
            key = 1

        response = make_response(render_template("hi.html", name=[{'name': name2}]))
        
        while True:
            cookie_id = f"id{key}"
            if not request.cookies.get(cookie_id):
                print("hellow")
                response.set_cookie(cookie_id, str(id2))  
                response.set_cookie('key', str(key)) 
                print('hellow')
                break
            key += 1
        session.clear()

        return response
    else:
         return render_template("fallure.html")
    


    
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        key = request.cookies.get('key')
        list1 = []
        list2 = []


        for i in range( 1 , int(key) + 1):
            list1 = db.execute("select name , mail , id from registants where id = ?" , str(request.cookies.get(f"id{i}")) )
            list2.extend(list1)

        return render_template("login.html", key = int(key) , list2 = list2)
    except:
        return render_template("fallure.html")

@app.route('/login/sent',methods=['POST', 'GET'])
def logedin():
    try:
        id = request.form.get('name')
        name = db.execute("select name from registants where id = ?" , id)
        return render_template("hi.html", name = name )    
    except:
        return render_template("fallure.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)                                                       
