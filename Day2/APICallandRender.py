import requests

r = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
json_response = r.json()
status = r.status_code
if status == 200:
    l = len(json_response["data"])
    for i in range(l):
        year = json_response["data"][i]["Year"]
        population = json_response["data"][i]["Population"]
        print(year,":",population)
else:
    print("Some Error Occured")