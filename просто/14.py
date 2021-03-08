import json
x = {"name":"Aidan",
      "age": 17,
      "city":"Url"
}
y = json.dumps(x)
print(type(y))