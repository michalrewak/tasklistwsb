from flask import Flask, render_template, redirect, url_for, request
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

app = Flask(__name__)
app.config["SECRET_KEY"] = "blabla"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
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
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
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
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("index"))

        return "<h1>Invalid username or password</h1>"
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method="sha256")
        new_user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        return "<h1>New user has been created!</h1>"
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template("signup.html", form=form)


@app.route("/add_new_task", methods=["GET", "POST"])
def new_task():  # put application's code here
    new_task = {}
    new_task["title"] = request.form["title"]
    new_task["description"] = request.form["description"]
    new_task["priority"] = request.form["priority"]
    new_task["assignee"] = request.form["assignee"]
    new_task["status"] = request.form["status"]
    db.session.add(new_task)
    db.session.commit()
    return render_template("create_new_task.html")


@app.route("/tasks", methods=["GET"])
def display_tasks():
    items = [
        {"id": "1", "title": "task1", "priority" : "niski", "assignee" : "Michał" },
        {"id": "2", "title": "task2", "priority" : "średni", "assignee" : "Andrzej"},
        {"id": "3", "title": "task3", "priority" : "średni", "assignee" : "Enrico"},
        {"id": "4", "title": "task4", "priority" : "średni", "assignee" : "Leonid"}
    ]
    return render_template("tasks.html", items=items)


if __name__ == "__main__":
    app.run(debug=False)
