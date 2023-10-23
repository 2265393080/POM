import json
import os


def json_read():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    json_path = os.path.join(cur_path, "data.json")
    with open(json_path, 'r', encoding='utf-8') as fp:
        return json.load(fp)


if __name__ == '__main__':
    print(json_read())
