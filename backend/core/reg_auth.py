import re
from json import dumps

import bcrypt
from flask import Response

from database.connect import create_session
from database.models.User import User
from database.models.UserData import UserData

SALT = b"$2b$12$SqoudaC3lp7Y2eKtEAchhe"


def registration(data):
    def __verification(data):
        if not re.match(r"[\w\.\-]+@[\w\-]+\.\w+", data["email"]):
            return False
        if not re.match(r"\w{3,}", data["firstname"]):
            return False
        if not re.match(r"\w{3,}", data["surname"]):
            return False
        with create_session() as session:
            user_found = (
                session.query(User)
                    .filter((User.email == data["email"]) | (User.login == data["login"]))
                    .first()
            )
            if user_found:
                return False

        return True

    if list(data.keys()) == [
        "firstname",
        "surname",
        "email",
        "login",
        "password",
        "age",
        "sex",
    ]:
        password = bcrypt.hashpw(password=data["password"].encode(), salt=SALT)
        if __verification(data):
            user = User(
                email=data["email"],
                login=data["login"],
                password=password.decode(),
            )
            user.create()

            user_data = UserData(
                user_id=user.id,
                name=data["firstname"],
                surname=data["surname"],
                age=data["age"],
                sex=data["sex"],
            )
            user_data.create()
            # Для демонстрации отношения один ко многим.
            user_data_one_more = UserData(
                user_id=user.id,
                name=data["firstname"] + "!",
                surname=data["surname"] + "!",
                age=data["age"],
                sex=data["sex"],
            )
            user_data_one_more.create()
            return Response(dumps({"result": "It's ok! User created."}), 200)
        else:
            return Response(dumps({"result": "You have not correct data."}), 400)
    else:
        return Response(dumps({"result": "error"}), 400)


def authentication(data):
    with create_session() as session:
        user_found = (
            session.query(User)
                .filter(
                (User.email == data["credentials"])
                | (User.login == data["credentials"])
            )
                .first()
        )
        if user_found and bcrypt.checkpw(
                data["password"].encode(), user_found.password.encode()
        ):
            return Response({"result": "It's ok!", "token": user_found.id}, 200)
    return Response({"result": "Data isn't correct"}, 401)


def get_profile_data(data):
    with create_session() as session:
        user_found = session.query(User).filter(UserData.user_id == data["id"]).first()
        if user_found:
            return Response(
                {
                    "name": user_found.name,
                    "surname": user_found.surname,
                    "age": user_found.age,
                    "sex": user_found.sex,
                },
                200,
            )
    return Response({"result": "Error"}, 500)


def change_user(data):
    with create_session() as session:
        user = session.query(User).filter(User.id == data["id"]).first()
        user_data = session.query(UserData).filter(UserData.user_id == data["id"]).first()
        if data["name"] == "email":
            user.email = data["value"]
            session.add(user)
        elif data["name"] == "login":
            user.email = data["value"]
            session.add(user)
        elif data["name"] == "name":
            user_data.name = data["value"]
            session.add(user_data)
        elif data["name"] == "surname":
            user_data.surname = data["value"]
            session.add(user_data)
        elif data["name"] == "age":
            user_data.age = data["value"]
            session.add(user_data)
        elif data["name"] == "sex":
            user_data.sex = data["value"]
            session.add(user_data)

        session.commit()
    return Response({}, 200)
