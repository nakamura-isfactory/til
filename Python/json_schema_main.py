#https://qiita.com/mink0212/items/8564d2ed5cf778d539c5

import json

import json
from jsonschema import validate, ValidationError

with open('schema.json') as file_obj:
    json_schema = json.load(file_obj)

item = {
    "kind":"cat",
    "name": "tama",
}
item = {
    "kind":"cat",
    "name": 12,
}

try:
    validate(item, json_schema)
except ValidationError as e:
    print(e.message)

print('END')
