from user import User

users = {
    User(1, 'admin', 'admin')
}

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    # if a user with the given username does not exist we can give a default value like None
    if user and user.password == password:
        return user


def identity(payload):  # payload is the content of the JWT token
    user_id = payload['identity']  # extract user id from the payload
    return userid_mapping.get(user_id, None)
