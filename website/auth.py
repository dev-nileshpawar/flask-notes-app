from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user
auth = Blueprint("auth", __name__)
from .models import User
from . import db

@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email = email).first()
        if user is not None:
            if check_password_hash(user.password, password):
                flash("Logged in successfully")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("incorrect password", category="error")
        else:
                flash("User not found", category="error" )
    return render_template("login.html" , text="Testing", user="Nilesh")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method =="POST":
        email = request.form.get("email")
        fname = request.form.get("fname")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user is not None:
            flash("Username is already taken", category="error")
        elif len(email)<5:
            flash("Email must be greater than 4 characters", category="error")
        elif len(password1) < 2:
            flash("Password must be greater than 4 characters", category="error")
        elif password2 != password1:
            flash("Password and confirm password does not match", category="error")
        elif len(fname)<5:
            flash("Name shuould be Atleast 5 char long", category="error")
        else:
            hashed = generate_password_hash(password1, method="pbkdf2:sha256")
            new_user = User(email=email, fname=fname, password = hashed )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created", category="success")
            login_user(new_user, remember=True)
            
            return redirect(url_for('views.home'))
            # add user to DB
    return render_template("register.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))