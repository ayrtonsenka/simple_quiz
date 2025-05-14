import requests

parameters = {
    "amount":50,
    "type": "boolean",
    "category":15
}

response = requests.get("https://opentdb.com/api.php", params=parameters)

question_data = response.json()

