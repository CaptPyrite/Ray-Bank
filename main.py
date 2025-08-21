from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  if not (session.get("auth_usr") or session.get("auth_passw")):
    return redirect("/login")
  
  else:
    return redirect('/dashboard')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
  if not (session.get("auth_usr") or session.get("auth_passw")):
    return redirect("/login")
    
  else:
    return render_template('/dashboard') 


@app.route("/register", methods=['GET', 'POST'])
def register():
  if request.method == "POST":
    session["auth_usr"] = request.form.get("usr")
    session["auth_passw"] = request.form.get("usr")
    return redirect("/")
  
  else:
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == "POST":
    session["auth_usr"] = request.form.get("usr")
    session["auth_passw"] = request.form.get("usr")
    return redirect("/")
  
  else:
    return render_template('login.html')


app.run(host="0.0.0.0",port=8080)
