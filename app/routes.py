from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm
from app import APP

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@APP.route("/registration", methods=['GET', 'POST'])
def registration():
    title = "LL - registration"
    form = RegistrationForm()
    if form.validate_on_submit():
        add_user(mongo, form.username.data, form.email.data, form.password.data)
        # flash()
    return render_template("registration.html", title = title, form = form)