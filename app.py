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

class members(db.Model):
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
        return '<members: {}>'.format(self.phone)



@app.route("/", methods=["GET", "POST"])
def member_register():
    if request.method == "POST":
        email   = request.form['email']  
        fname   = request.form['fname']
        lname   = request.form['lname']
        phone   = request.form['phone']
        designation  = request.form['designation']
        gender  = request.form['gender']
        address  = request.form['address']
        membersid  = request.form['membersid']
        birthday  = request.form['birthday']
        section  = request.form['section']

        member = members(email=email, fname=fname, lname=lname, phone=phone, designation=designation,\
        gender=gender, address=address, membersid=membersid, birthday=birthday, section=section)
        
        # check = members.query.filter_by(phone=phone).first()
        # # if check is not None:
        # #     return redirect(url_for("index"))
        try:
            db.session.add(member)
            db.session.commit()
            flash('You have successfully added a new employee.')
        except:
            flash('Error: employee name already exists.')

        return redirect(url_for("register"))
    return render_template("index.html")



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