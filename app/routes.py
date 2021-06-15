from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.forms import LoginForm, RegistrationForm
from app import APP
from app.models import User

@APP.route('/')
@APP.route('/index')
def index():
    user = {'nickname': 'Guest'}
    posts = [ # список выдуманных постов
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@APP.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return(redirect(url_for('login')))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)


@APP.route("/registration", methods=['GET', 'POST'])
def registration():
    title = "LL - registration"
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user(mongo, form.username.data, form.email.data, form.password.data)
        # flash()
    return render_template("registration.html", title = title, form = form)