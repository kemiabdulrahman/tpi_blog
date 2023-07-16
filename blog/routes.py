from blog import app, bcrypt, db
from flask import  flash, redirect, render_template, url_for
from blog.models import User, Post
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, current_user, logout_user

posts = [
  {
           'author':'Jane Doe',
            'title':'Blog Post 1',
            'content':'First Content Post',
            'date_posted':'April, 20 2031',
            },
       


 {
           'author':'Johnny Bane',
            'title':'Blog Post 2',
            'content':'Second post Content',
            'date_posted':'May 7, 2012',
            }

        ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template('about.html')



@app.route("/contact")
def contact():
    return render_template('contact.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to login", category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
#       Checking if the user exist Comparing database password to the hashed password
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You have been logged in Successfully", 'success')
            return redirect(url_for('home'))
        else:
            flash("Unsuccessful Login!", 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))



@app.route("/account")
@login_required
def account():
    return render_template(url_for("account.html"), title="Account")
