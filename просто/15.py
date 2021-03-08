import json
x = {
    "name":"Aidan",
    "age":17,
    "married": False,
    "divorced": False,
    "children": ("Tayir"),
    "pets": ("Retriver", "Dinosaur"),
    "cars": [
        {"model": "Porshe Cayenne"},
        {"model": "Mercedes Benz S class"}
    ]
}
print(json.dumps(x))