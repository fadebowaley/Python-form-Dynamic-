from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    fname = db.Column(db.String(60), index=True)
    lname = db.Column(db.String(60), index=True)
    phone = db.Column(db.String(16), index=True)
    designation = db.Column(db.String(200), index=True)
    gender = db.Column(db.String(60), index=True)
    address = db.Column(db.String(200), index=True)
    membersid = db.Column(db.String(16), index=True)
    birthday = db.Column(db.DateTime)
    section = db.Column(db.String(200), index=True)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)







@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    
    db.create_all()
    app.run(debug=True)