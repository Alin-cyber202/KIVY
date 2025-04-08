import requests

url = "https://kivy.org/protected_page"  
response = requests.get(url)

if response.status_code == 200:
    print("Защищенная страница доступна без авторизации!")
else:
    print("Доступ к защищенной странице запрещен.")
      
