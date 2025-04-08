from locust import HttpUser, task, between

class VolumeUser(HttpUser):
       wait_time = between(1, 5)  

       @task
       def load_large_data(self):
           # Заменить на URL, который возвращает большой объём данных
           self.client.get("https://kivy.org/doc/stable/gettingstarted/installation.html")
   
