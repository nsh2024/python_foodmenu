import json
from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def createUser(user):
    import json
    from json import JSONEncoder


def read_user_data():
    user_data_filename = 'data/users.json'
    user_data_file = open(user_data_filename)
    json_user_data = user_data_file.read()
    users = json.loads(json_user_data).get("users")
    for i in range(len(users)):
        print(users[i].get("username"))
    return users


def write_menu_data(user):
    users_list = read_user_data()
    for i in range(len(users_list)):
        print(users_list[i].get("username"))

    # user = {"username": "ns", "password": "123XD12"}
    users_list.append(user)

    users_data_filename = 'data/users.json'
    with open(users_data_filename, 'w') as dataFile:
        json.dump({"users": list(users_list)}, dataFile, indent=4, separators=(',', ': '), cls=UserEncoder)

    return read_user_data()
