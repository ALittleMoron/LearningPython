import json


def save_json_file(data:dict) -> None:
    with open('data.json', 'w') as jf:
        json.dump(data, jf)


def read_json_file() -> None:
    with open('data.json', 'r') as jf:
        print(json.load(jf))

if __name__ == '__main__':
    data = [{'name': 'alex', 'age': 25, 'gender': 'male'},
            {'name': 'anna', 'age': 15, 'gender': 'female'}]
    read_json_file()
