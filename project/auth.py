from flask import Blueprint, render_template, request,redirect,url_for,session
from project import app
from project.models import Account,db
import re

@app.route("/base")
def base():
    return render_template('base.html')
    

@app.route("/register", methods = ["GET", "POST"])
def register():
    message = ''
    if request.method == 'POST':
        nom = request.form.get('name')
        prenom = request.form.get('first_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form['confirm_password']
        user= Account.query.filter_by(email=email).first()
        longueur=len(password)

        if user:
            message = 'account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid address!'
        elif  not nom or not prenom or not  password or not email:
            message = 'Please fill out the form'  
        elif password != confirm_password:
            message = 'Incorrect password please re-enter it! '
        elif longueur<=4:
           message='password is too short !'
        elif not re.match(r'[A-Za-z]+', nom):
            message = 'the name must only consist of characters!'
        elif not re.match(r'[A-Za-z]+',prenom):
            message = 'the first name must only consist of characters!'
        else:
            new_user = Account(name=nom,first_name=prenom,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            message = 'you have been successfully registered'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
        return redirect(url_for("login"))
    return render_template('register.html', message = message)

@app.route("/login", methods = ["GET", "POST"])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = Account.query.filter_by(email=email).first()
        user2= Account.query.filter_by(password=password).first()
        if user and user2: 
           message = 'Logged successfully!'
           return render_template('profile.html',message=message)
        elif not user:
            message = 'incorrect email ! please verify your e-mail'
        elif not user2:
            message = 'incorrect password! please verify your password'  
    return render_template('login.html', message = message)


@app.route('/profile')
def profile():
    return redirect('/login')
    return render_template('profile.html')
    
@app.route("/logout")
def logout():
    return redirect(url_for('login'))
   
@app.route('/Produit')
def Produit():
    return render_template('Produit.html')