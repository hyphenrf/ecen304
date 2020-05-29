#!/usr/bin/env python3

from flask import Flask, request, session
from auth import _auth, hashed, verify_email
from backend.models import *

import queries as quer

endpoints = {
    "GET": [
        "/authors",
        "/authors?filterBy=name",
        "/authors?sortBy=name:asc",
        "/authors?sortBy=name:desc",
        "/author/:id",
        "/books",
        "/books?filterBy=name",
        "/books?sortBy=name:asc",
        "/books?sortBy=name:desc",
        "/books?sortBy=price:asc",
        "/books?sortBy=price:desc",
        "/book/:id",
        "/users",
        "/users?filterBy=name",
        "/users?sortBy=name:asc",
        "/users?sortBy=name:desc"
        "/user/:id",
    ],
    "POST": [
        "/author/create",
        "/book/create",
        "/user/signup"
        "/user/login",
        "/user/logout?id",
    ],
    "DELETE": [
        "/author/remove?id",
        "/book/remove?id",
        "/user/remove?id"
    ],
    "PUT": [
        "/author/edit?id",
        "/book/edit?id",
        "/user/edit?id"
    ]
}

admin_tokens = set(quer.admins())
def auth(sesh): return _auth(sesh, admin_tokens)


this = Flask(__name__)
this.secret_key = b"some random bytes"
salt = "some salt"
session['logged_in'] = False

@this.route("/")
def index():
    return endpoints

# Things that don't need to be authed
@this.route("/user/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    passw = data.get("password")
    name = data.get("name")
    visa = int(data.get("visa"))
    addr = data.get("address")
    birth = data.get("birth")

    if all([email, passw, name]):
        verify_email(email) or return {"status": "error: bad email"}
        len(passw) > 8 or return {"status": "error: bad password"}
        passw = hashed(salt+passw)
        user = User(
            name = name
            email = email
            password = passw
            visa = visa
            birth = birth
            address = addr
        )
        #TODO: db commit code
        return {"status": "success"}
    else:
        return {"status": "error: missing fields"}

@this.route("/user/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    passw = data.get("password")

    if email and passw:
        user = quer.actor_by_email(email)
        if user.password == hashed(salt+passw):
            session['id'] = user.id
            session['logged_in'] = True
            return {"status": "success"}
        else:
            return {"status": "error: invalid login"}



# Things that need to be authed
@this.route("/user/logout", methods=["POST"])
def logout():
    id = request.args.get('id')
    if session['logged_in']:
        session['id'] == id or return {"status": "error: forbidden"}
        session.pop('id')
        session['logged_in'] = False
        return {"status": "succesS"}
    else:
        return {"status": "error: not logged in"}

@this.route("/user/<str:operation>", methods=["DELETE", "PUT"])
@auth(session)
def up_del_user(operation):
    id = request.args['id']
    fields = request.json
    method = request.method
    
    if operation == "edit" and method == "PUT":
        return quer.update("user", id, fields)
    else if operation == "remove" and method == "DELETE": 
        return quer.delete("user", id)
    else:
        return {"status": "error: improper operation"}

@this.route("/users", methods=["GET"])
@auth(session)
def users():
    name = request.args.get('filterBy')
    sortby = request.args.get('sortBy')
    return quer.users(sort=sortby, match=name)

@this.route("/<str:object>/<str:operation>", methods=["POST","DELETE","PUT"])
@auth(session)
def up_del(object, operation):
    id = request.args['id']
    fields = request.json
    method = request.method

    if object not in {"book", "author"}:
        return {"status": "error: improper endpoint"}
    else if operation == "edit" and method == "PUT":
        return quer.update(object, id, fields)
    else if operation == "remove" and method == "DELETE": 
        return quer.delete(object, id)
    else if operation == "create" and method == "POST":
        return quer.add(object, id, fields)
    else:
        return {"status": "error: improper operation"}


if __name__ == "__main__":
    this.run(host="0.0.0.0", port="42060")
