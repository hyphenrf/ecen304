#!/usr/bin/env python3

from flask import Flask, request
from auth import _auth
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
        "/user/create"
        "/user/login",
        "/user/logout/:id",
    ],
    "DELETE": [
        "/author/remove?id",
        "/book/remove?id",
        "/user/remove?id"
    ],
    "PATCH": [
        "/author/edit?id",
        "/book/edit?id",
        "/user/edit?id"
    ]
}

tokens = {}
def auth(req): return _auth(req, tokens)


this = Flask(__name__)

@this.route("/")
def index():
    return endpoints

# Things that need to be authed
@this.route("/users", methods=["GET"])
def users():
    @auth(request)
    def authorized():
        name = request.args.get('filterBy')
        sortby = request.args.get('sortBy')

    pass

@this.route("/user/<operation>", methods=["GET","POST","PATCH"])
@auth(request.json['token']):

@this.route("/book/<operation>", methods=["GET","POST","PATCH"])
@auth

@this.route("/author/<operation>", methods=["GET","POST","PATCH"])
@auth


if __name__ == "__main__":
    this.run(host="0.0.0.0", port="42060")
