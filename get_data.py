# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

# request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
# response = requests.get(request_url)
# #print(response.status_code)
# parsed_response = json.loads(response.text)
# print(parsed_response["name"])


# request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
# response = requests.get(request_url)
# print(response.status_code)
# parsed_response2 = json.loads(response.text)
# for p in parsed_response2:
#     print(p["name"], p["id"])

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response = requests.get(request_url)
print(response.status_code)
parsed_response3 = json.loads(response.text)


grades = []
students = parsed_response3["students"]
for x in students:
    grades.append(x["finalGrade"])

print(max(grades))
print(min(grades))
print(sum(grades)/len(grades))


import json
import requests
import statistics
print("----------")
print("PART 1")
product_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json")
product = json.loads(product_response.text)
print(product["name"])
print("----------")
print("PART 2")
products_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json")
products = json.loads(products_response.text)
for p in products:
    print(p["name"])
print("----------")
print("PART 3")
gradebook_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json")
gradebook = json.loads(gradebook_response.text)
#print(gradebook)
#breakpoint()
grades = [s["finalGrade"] for s in gradebook["students"]]
print("MIN:", min(grades))
print("MAX:", min(grades))
print("AVG:", statistics.mean(grades))


