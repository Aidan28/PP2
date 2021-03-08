import json
data = input()
json_data = json.loads(data)
ans, ans_name, mn = 0, '', 999999

for item in json_data["Subscriptions"]:
    price = int(item["price"])
    discount = int(item["discount"])
    ans = int(price * (100 - discount) / 100)
    if mn > ans:
        mn = ans
        ans_name = str(item["item"])

print('Name: ' + ans_name)
print('Price: ' + str(mn))