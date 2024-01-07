import json
from json import JSONEncoder


class MenuItemEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def read_menu_data():
    dataFileName = 'data/menus.json'
    menuDataFile = open(dataFileName)
    jsonData = menuDataFile.read()
    menus = json.loads(jsonData)
    menu_list = menus.get("menus");
    for i in range(len(menu_list)):
        print(menu_list[i].get("date"))
    return menu_list


def write_menu_data(menu):
    menu_list = read_menu_data()
    for i in range(len(menu_list)):
        print(menu_list[i].get("date"))

    # menu = {"date": "07-01-2024", "menu": {"breakfast": "idly", "lunch": "sambar", "dinner": "dosai", "lunchBox": "pasta"}}
    menu_list.append(menu)

    dataFileName = 'data/menus.json'
    with open(dataFileName, 'w') as dataFile:
        json.dump({"menus": list(menu_list)}, dataFile, indent=4, separators=(',', ': '), cls=MenuItemEncoder)

    return read_menu_data()
