#!/usr/bin/python3
from models.base import Base
import json
print("Checking if all classes method are working fine")

python_list = Base.from_json_string([{'id': 4}])
print(type(python_list))

json_string = Base.to_json_string([{'id': 4}])
print(type(json_string))

json_list = json.dumps([{'id': 89}])
json_list_1 = json.dumps([{'id': 33}])

print(type(json_list), type(json_list_1))
