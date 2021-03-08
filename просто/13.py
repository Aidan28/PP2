import json
x = '{"name":"Aidan", "age":17, "city":"Url"}'
y = json.loads(x)
print(y["age"])