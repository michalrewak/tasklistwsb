from flask import Flask, render_template, redirect, url_for, request, session
import flask_login
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
import dbmanager

app = Flask(__name__)
app.config["SECRET_KEY"] = "blabla"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
bootstrap = Bootstrap(app)
test = dbmanager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



class User(UserMixin):
    def __init__(self, id, email):
        self.id = int(id)
        self.email = str(email)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id, test.userEmail(user_id))


class LoginForm(FlaskForm):
    email = StringField(
        "email", validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )
    remember = BooleanField("remember me")


class RegisterForm(FlaskForm):
    email = StringField(
        "email",
        validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)],
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        userId = test.loginUser(form.email.data, form.password.data)
        if userId != -1:
            session['_user_id'] = userId
            user = User(userId, test.userEmail(id))
            login_user(user, remember=form.remember.data)
            return redirect(url_for("index"))

        return "<h1>Invalid email or password</h1>"
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        test.createUser(form.email.data, form.password.data)
        return "<h1>New user has been created!</h1>"
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template("signup.html", form=form)


@app.route("/add_new_task", methods=["GET", "POST"])
def new_task():  # put application's code here
    # new_task = {}
    # new_task["title"] = request.form["title"]
    # new_task["description"] = request.form["description"]
    # new_task["priority"] = request.form["priority"]
    # new_task["assignee"] = request.form["assignee"]
    # new_task["status"] = request.form["status"]
    # db.session.add(new_task)
    # db.session.commit()
    return render_template("create_new_task.html")


@app.route("/tasks", methods=["GET"])
def tasks_list():
    if '_user_id' not in session:
        return redirect("signup")

    userid = flask_login.current_user._get_current_object().id
    tasks = test.getTasks(userid)

    return render_template("tasks.html", items=tasks)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
