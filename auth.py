
def _auth(request, tokens):
    token = request.json.get('token')
    def auth_inner(fn):
        def wrap(*args, **kwargs):
            if token in tokens:
                return fn(*args, **kwargs)
            else:
                return {"error": "forbidden"}
        return wrap
    return auth_inner

