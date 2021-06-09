from flask import Flask, request, Response, render_template

from core.reg_auth import registration, authentication, get_profile_data, change_user
from database.connect import engine, Base
from database.models import User, UserData, UserTrash, Trash

Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_route():
    return render_template('index.html')


@app.route("/reg", methods=["GET"])
def reg_route():
    return render_template('reg.html')


@app.route("/auth", methods=["GET"])
def auth_route():
    return render_template('auth.html')


@app.route("/profile", methods=["GET"])
def profile_route():
    return render_template("profile.html")


@app.route("/reg", methods=["POST"])
def reg():
    return registration(request.form)


@app.route("/auth", methods=["POST"])
def auth():
    return authentication(request.form)


@app.route("/profile", methods=["POST"])
def profile():
    return get_profile_data(request.data)


@app.route("/other", methods=["GET"])
def change():
    return render_template("other.html")


@app.route("/other", methods=["POST"])
def change_field():
    print(request.form)
    return change_user(request.form)


if __name__ == "__main__":
    app.run()
